import pygame
from random import randrange
pygame.init()
level = 1
mon = 800
size = 50
fps = 60
bg = pygame.image.load("C:\programmingFORbss\pp2\pp2-21B030328\lab9\images\game_background.jpg")
bg = pygame.transform.scale(bg, (800, 800))
x, y = 300, 300
length = 1
snake = [(x, y)]

buttons = {
    'w': True,
    'a': True,
    'd': True,
    's': True
}

front = pygame.font.SysFont('Ariel', 26, True)
count = 0

walls = {  # уровни препятствий,
    1: [(50, 50), (50, 100), (50, 150), (50, 200), (150, 0), (200, 0), (250, 0), (500, 500), (550, 500), (500, 550),
        (600, 500), (650, 500)],
    2: [(700, 700), (650, 700), (700, 650), (600, 700), (700, 600), (700, 550), (650, 550), (650, 500)],
    3: [(0, 0), (50, 0), (100, 0), (150, 0), (200, 0), (250, 0), (300, 0), (350, 0), (400, 0), (450, 0), (500, 0),
        (550, 0), (600, 0), (650, 0), (700, 0), (0, 50), (0, 100), (0, 150), (0, 200), (0, 250), (0, 300), (0, 350),
        (0, 400), (0, 450), (0, 500), (0, 550), (0, 600), (0, 650), (0, 700)]
}

speed = 7
sup = 10  # чтобы узнать попадает ли score в range
score = 0
dx, dy = 0, 0

clock = pygame.time.Clock()
time = 50

apple = randrange(50, mon, size), randrange(0, mon, size)

while apple in walls:
    apple = randrange(50, mon, size), randrange(0, mon, size)

level1 = 9
level2 = 20

screen = pygame.display.set_mode([mon, mon])

score_font = pygame.font.SysFont("Verdana", 20)

working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
#Нужно для проверки чтобы если мы идем на право то не могли идти на лево, если на верх то вниз
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and buttons['w']:
                buttons = {
                    'w': True,
                    'a': True,
                    'd': True,
                    's': False
                }
                dx, dy = 0, -1
            elif event.key == pygame.K_s and buttons['s']:
                dx, dy = 0, 1
                buttons = {
                    'w': False,
                    'a': True,
                    'd': True,
                    's': True
                }
            elif event.key == pygame.K_a and buttons['a']:
                dx, dy = -1, 0
                buttons = {
                    'w': True,
                    'a': True,
                    'd': False,
                    's': True
                }
            elif event.key == pygame.K_d and buttons['d']:
                dx, dy = 1, 0
                buttons = {
                    'w': True,
                    'a': False,
                    'd': True,
                    's': True
                }
    screen.blit(bg, (0, 0))
#если змейка ударяется об стену то игра заканчивается
    if snake[-1] in walls[level]:
        pygame.quit()

    if apple in walls[level]:  # нужна для проверки если яблоко появилось внутри стен
        apple = randrange(50, mon, size), randrange(0, mon, size)

    [(pygame.draw.rect(screen, pygame.Color('blue'), (i, j, size - 2, size - 2))) for i, j in snake]  # рисуем змейку

    pygame.draw.rect(screen, pygame.Color('red'), (*apple, size - 2, size - 2))  # рисуем яблоко

    for i in walls[level]:  # рисуем стены определенного уровня
        pygame.draw.rect(screen, (0, 0, 0), (i[0], i[1], 48, 48))
    render_score = front.render(f'SCORE:{count}', 1, pygame.Color('white'))  # пишем score
    screen.blit(render_score, (5, 5))  # рисуем score

    if time == 0:  # время для случая, если время для сьедания яблока истекло
        apple = randrange(50, mon, size), randrange(0, mon, size)
        time = 50

    x += dx * size  # непрерывное движение
    y += dy * size

    time -= 1  # раз в 50 speed мы обновляем местоположение яблоки, это нужно нам для 111 строки

    snake.append((x, y))  # координаты змейки

    snake = snake[-length:]  # для того чтобы мы брали только змейку, а не места где она прошлась

    if count in range(level1,
                      level2):  # нужна для переноса в след уровень,а так же для увеличения награды за яблоко, скорость,
        level1 += sup
        level2 += sup
        sup += 20
        level += 1
        score += 1
        speed += 2
        if level == 4: level = 1
    render_score_level = front.render(f'LEVEL:{level}', 1, 'white')
    screen.blit(render_score_level, (100, 5))
    if snake[-1] == apple:  # в случае если координата яблоки и головы змейки совпала
        count += randrange(1,5)
        length += 1
        time = 50
        apple = randrange(50, mon, size), randrange(0, mon, size)

    if x < 0 or x > mon - size or y < 0 or y > mon - size or len(snake) != len(
            set(snake)):  # выход за пределы поля или змейка входит в себя
        working = False

    pygame.display.flip()
    clock.tick(speed)