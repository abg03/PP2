import pygame
import sys
import random
import psycopg2
import time
import json
from enum import Enum

# Параметры подключения к базе данных
DB_NAME = "snake_game_db"
DB_USER = "bmk"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = "5432"

# Константы игры
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# Направления
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

# Уровни игры
class Level:
    def __init__(self, level_num, speed, walls=None):
        self.level_num = level_num
        self.speed = speed
        self.walls = walls if walls else []

# Класс для работы с базой данных
class Database:
    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT
            )
            self.create_tables()
        except psycopg2.Error as e:
            print(f"Ошибка подключения к базе данных: {e}")
            sys.exit(1)

    def create_tables(self):
        """Создает необходимые таблицы для игры"""
        try:
            cur = self.conn.cursor()
            
            # Создание таблицы для пользователей
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            
            # Создание таблицы для очков
            cur.execute("""
                CREATE TABLE IF NOT EXISTS user_scores (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id),
                    score INTEGER NOT NULL,
                    level INTEGER NOT NULL,
                    saved_state JSONB,
                    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            
            self.conn.commit()
            print("Таблицы игры успешно созданы")
        except psycopg2.Error as e:
            print(f"Ошибка при создании таблиц: {e}")
            self.conn.rollback()

    def get_or_create_user(self, username):
        """Получает или создает пользователя"""
        try:
            cur = self.conn.cursor()
            
            # Проверка существования пользователя
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            
            if user:
                return user[0]
            else:
                # Создание нового пользователя
                cur.execute(
                    "INSERT INTO users (username) VALUES (%s) RETURNING id",
                    (username,)
                )
                user_id = cur.fetchone()[0]
                self.conn.commit()
                return user_id
        except psycopg2.Error as e:
            print(f"Ошибка при работе с пользователем: {e}")
            self.conn.rollback()
            return None

    def get_user_level(self, user_id):
        """Получает текущий уровень пользователя"""
        try:
            cur = self.conn.cursor()
            
            # Получение максимального уровня
            cur.execute("""
                SELECT MAX(level) FROM user_scores 
                WHERE user_id = %s
            """, (user_id,))
            
            level = cur.fetchone()[0]
            
            return level if level else 1
        except psycopg2.Error as e:
            print(f"Ошибка при получении уровня: {e}")
            return 1

    def save_score(self, user_id, score, level, saved_state=None):
        """Сохраняет счет пользователя"""
        try:
            cur = self.conn.cursor()
            
            # Сохранение счета
            if saved_state:
                cur.execute("""
                    INSERT INTO user_scores (user_id, score, level, saved_state)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, score, level, saved_state))
            else:
                cur.execute("""
                    INSERT INTO user_scores (user_id, score, level)
                    VALUES (%s, %s, %s)
                """, (user_id, score, level))
            
            self.conn.commit()
            print(f"Счет {score} на уровне {level} сохранен")
        except psycopg2.Error as e:
            print(f"Ошибка при сохранении счета: {e}")
            self.conn.rollback()

    def get_saved_state(self, user_id):
        """Получает сохраненное состояние игры"""
        try:
            cur = self.conn.cursor()
            
            # Получение последнего сохраненного состояния
            cur.execute("""
                SELECT saved_state FROM user_scores 
                WHERE user_id = %s AND saved_state IS NOT NULL
                ORDER BY played_at DESC LIMIT 1
            """, (user_id,))
            
            result = cur.fetchone()
            
            return result[0] if result else None
        except psycopg2.Error as e:
            print(f"Ошибка при получении сохраненного состояния: {e}")
            return None

    def close(self):
        """Закрывает соединение с базой данных"""
        if self.conn:
            self.conn.close()

# Класс для игры "Змейка"
class SnakeGame:
    def __init__(self, username):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Змейка')
        self.font = pygame.font.SysFont('Arial', 24)
        
        # Инициализация базы данных
        self.db = Database()
        self.user_id = self.db.get_or_create_user(username)
        self.username = username
        
        # Получение уровня игрока
        self.current_level_num = self.db.get_user_level(self.user_id)
        
        # Создание уровней
        self.levels = self.create_levels()
        
        # Инициализация игры
        self.reset_game()
        
        # Проверка на сохраненное состояние
        saved_state = self.db.get_saved_state(self.user_id)
        if saved_state:
            self.load_game_state(saved_state)

    def create_levels(self):
        """Создает уровни игры"""
        levels = {}
        
        # Уровень 1: Без стен, низкая скорость
        levels[1] = Level(1, 10)
        
        # Уровень 2: Базовые стены, средняя скорость
        walls2 = []
        for i in range(10, 30):
            walls2.append((i, 10))
            walls2.append((i, 20))
        levels[2] = Level(2, 12, walls2)
        
        # Уровень 3: Сложные стены, высокая скорость
        walls3 = []
        for i in range(5, 35):
            if i % 2 == 0:
                walls3.append((i, 5))
                walls3.append((i, 25))
            if i % 3 == 0:
                walls3.append((10, i))
                walls3.append((30, i))
        levels[3] = Level(3, 15, walls3)
        
        return levels

    def reset_game(self):
        """Сбрасывает игру в начальное состояние"""
        # Уровень
        self.set_level(self.current_level_num)  # Ensure level is set before placing food

        # Начальное положение змейки в центре экрана
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.snake_direction = Direction.RIGHT

        # Случайное расположение еды
        self.place_food()

        # Счет
        self.score = 0

        # Игра на паузе?
        self.paused = False
        # Игра окончена?
        self.game_over_state = False

    def set_level(self, level_num):
        """Устанавливает текущий уровень"""
        if level_num in self.levels:
            self.current_level_num = level_num
            self.level = self.levels[level_num]
        else:
            # Если запрошенный уровень не существует, используем последний
            max_level = max(self.levels.keys())
            self.current_level_num = max_level
            self.level = self.levels[max_level]

    def place_food(self):
        """Размещает еду в случайном месте, не занятом змейкой или стенами"""
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            
            # Проверяем, что место не занято змейкой или стеной
            if (x, y) not in self.snake and (x, y) not in self.level.walls:
                self.food = (x, y)
                break

    def handle_events(self):
        """Обрабатывает события клавиатуры"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.db.close()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.game_over_state:
                    if event.key == pygame.K_RETURN:
                        self.reset_game()
                else:
                    if event.key == pygame.K_UP and self.snake_direction != Direction.DOWN:
                        self.snake_direction = Direction.UP
                    elif event.key == pygame.K_DOWN and self.snake_direction != Direction.UP:
                        self.snake_direction = Direction.DOWN
                    elif event.key == pygame.K_LEFT and self.snake_direction != Direction.RIGHT:
                        self.snake_direction = Direction.LEFT
                    elif event.key == pygame.K_RIGHT and self.snake_direction != Direction.LEFT:
                        self.snake_direction = Direction.RIGHT
                    elif event.key == pygame.K_p:  # Пауза и сохранение
                        self.paused = not self.paused
                        if self.paused:
                            self.save_game_state()

    def move_snake(self):
        """Двигает змейку в текущем направлении"""
        if self.paused or self.game_over_state:
            return
            
        head_x, head_y = self.snake[0]
        
        if self.snake_direction == Direction.UP:
            new_head = (head_x, head_y - 1)
        elif self.snake_direction == Direction.DOWN:
            new_head = (head_x, head_y + 1)
        elif self.snake_direction == Direction.LEFT:
            new_head = (head_x - 1, head_y)
        elif self.snake_direction == Direction.RIGHT:
            new_head = (head_x + 1, head_y)
        
        # Проверка на столкновение со стеной или границей экрана
        if (new_head in self.snake or 
            new_head in self.level.walls or
            new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            self.game_over()
            return
        
        # Двигаем змейку
        self.snake.insert(0, new_head)
        
        # Проверяем, съела ли змейка еду
        if new_head == self.food:
            self.score += 10
            self.place_food()
            
            # Повышаем уровень при достижении определенного счета
            if self.score >= self.current_level_num * 50 and self.current_level_num < max(self.levels.keys()):
                self.current_level_num += 1
                self.set_level(self.current_level_num)
                self.db.save_score(self.user_id, self.score, self.current_level_num)
        else:
            self.snake.pop()  # Удаляем хвост, если не съели еду

    def draw(self):
        """Отрисовывает игру"""
        self.screen.fill(BLACK)
        
        # Рисуем змейку
        for segment in self.snake:
            pygame.draw.rect(self.screen, GREEN, 
                             (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, 
                              GRID_SIZE, GRID_SIZE))
        
        # Рисуем еду
        pygame.draw.rect(self.screen, RED,
                         (self.food[0] * GRID_SIZE, self.food[1] * GRID_SIZE,
                          GRID_SIZE, GRID_SIZE))
        
        # Рисуем стены
        for wall in self.level.walls:
            pygame.draw.rect(self.screen, GRAY,
                             (wall[0] * GRID_SIZE, wall[1] * GRID_SIZE,
                              GRID_SIZE, GRID_SIZE))
        
        # Отображаем информацию
        score_text = self.font.render(f'Счет: {self.score}', True, WHITE)
        level_text = self.font.render(f'Уровень: {self.current_level_num}', True, WHITE)
        user_text = self.font.render(f'Игрок: {self.username}', True, WHITE)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 40))
        self.screen.blit(user_text, (10, 70))
        
        # Если игра на паузе
        if self.paused:
            pause_text = self.font.render('ПАУЗА - Нажмите P для продолжения', True, WHITE)
            text_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(pause_text, text_rect)
        
        # Если игра окончена
        if self.game_over_state:
            game_over_text = self.font.render('ИГРА ОКОНЧЕНА - Нажмите ENTER для перезапуска', True, WHITE)
            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(game_over_text, text_rect)
        
        pygame.display.flip()

    def game_over(self):
        """Обрабатывает окончание игры"""
        self.game_over_state = True
        # Сохраняем финальный счет
        self.db.save_score(self.user_id, self.score, self.current_level_num)
        print(f"Игра окончена! Финальный счет: {self.score}")

    def save_game_state(self):
        """Сохраняет текущее состояние игры в базу данных"""
        # Преобразуем Direction в строку для сериализации
        direction_str = str(self.snake_direction.name)
        
        # Создаем словарь состояния
        state = {
            'snake': self.snake,
            'direction': direction_str,
            'food': self.food,
            'score': self.score,
            'level': self.current_level_num
        }
        
        # Сохраняем в базу данных
        self.db.save_score(self.user_id, self.score, self.current_level_num, json.dumps(state))
        print("Игра сохранена")

    def load_game_state(self, saved_state):
        """Загружает сохраненное состояние игры"""
        try:
            state = saved_state
            
            # Загружаем состояние
            self.snake = state['snake']
            self.snake_direction = Direction[state['direction']]
            self.food = tuple(state['food'])
            self.score = state['score']
            self.set_level(state['level'])
            
            print("Игра загружена из сохранения")
        except Exception as e:
            print(f"Ошибка при загрузке состояния: {e}")
            self.reset_game()

    def run(self):
        """Запускает игровой цикл"""
        while True:
            self.handle_events()
            self.move_snake()
            self.draw()
            self.clock.tick(self.level.speed)

# Главная функция для запуска игры
def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Змейка - Вход')
    font = pygame.font.SysFont('Arial', 24)
    
    # База данных для проверки соединения
    try:
        db = Database()
        db.close()
    except Exception as e:
        print(f"Не удалось подключиться к базе данных: {e}")
        pygame.quit()
        sys.exit(1)
    
    # Ввод имени пользователя
    username = ""
    active = True
    
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    # Добавляем только печатные символы
                    if event.unicode.isprintable() and len(username) < 20:
                        username += event.unicode
        
        screen.fill(BLACK)
        
        # Отображаем инструкцию
        title_text = font.render('Игра "Змейка"', True, WHITE)
        instruction_text = font.render('Введите ваше имя пользователя:', True, WHITE)
        username_text = font.render(username, True, GREEN)
        enter_text = font.render('Нажмите ENTER для начала игры', True, WHITE)
        
        screen.blit(title_text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 100))
        screen.blit(instruction_text, (WINDOW_WIDTH // 2 - 180, WINDOW_HEIGHT // 2 - 50))
        screen.blit(username_text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2))
        screen.blit(enter_text, (WINDOW_WIDTH // 2 - 180, WINDOW_HEIGHT // 2 + 50))
        
        pygame.display.flip()
    
    # Запускаем игру
    game = SnakeGame(username)
    game.run()

if __name__ == "__main__":
    main()