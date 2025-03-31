import pygame

pygame.init()
Width, Height = 800, 800
lastPos = (0, 0)
screen = pygame.display.set_mode((Width, Height))
prev, cur = None, None
drawing = False
start_pos = 0
end_pos = 0
game_over = True
FPS = 30
color = 'black'
clock = pygame.time.Clock()
screen.fill('white')#закрашиваем наш пэйнт в белый фон
mode = 'pen'#это будет нашим выбором фигур
pygame.display.set_caption('Paint')#название игры


def clear():
    screen.fill('white')#очистить экран


def circle(screen, color, start, end):#рисование круга
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, color, (x, y), radius, 5)


def rect(screen, color, start, end):#рисование прямоугольника

    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    width = abs(x1 - x2)
    height = abs(y1 - y2)
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, color, (x1, y1, width, height), 3)
    if y2 > y1 and x1 > x2:
         pygame.draw.rect(screen, color, (x2, y1, width, height), 3)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, color, (x2, y2, width, height), 3)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, color, (x1, y2, width, height), 3)


def sq(screen, color, start, end):#рисование квадрата
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    mn = min(abs(x2 - x1), abs(y2 - y1))

    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, color, (x1, y1, mn, mn), 5)
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, color, (x2, y1, mn, mn), 5)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, color, (x2, y2, mn, mn), 5)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, color, (x1, y2, mn, mn), 5)


def right_triangle(screen, color, start, end):#рисование прямоугольного треугольника
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    if x2 > x1 and y2 > y1:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x1, y2)), 5)
    if y2 > y1 and x1 > x2:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x1, y2)), 5)
    if x1 > x2 and y1 > y2:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x2, y1)), 5)
    if x2 > x1 and y1 > y2:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x2, y1)), 5)


def equilateral_triangle(screen, color, start, end):#рисование равностороннего треугольника
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    width_b = abs(x2 - x1)
    height = (3 ** 0.5) * width_b / 2

    if y2 > y1:
        pygame.draw.polygon(screen, color, ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), 5)
    else:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)), 5)


def rhombus(screen, color, start, end):#рисование ромба
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    pygame.draw.lines(screen, pygame.Color(color), True,
                      (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), 5)


while game_over:
    mouse_movement = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 725 and mouse_movement[1] <= 75 and \
                mouse_movement[0] <= 750 and mouse_movement[1] >= 45:#координаты нахождения ручки
            mode = 'pen'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 400 and mouse_movement[1] <= 70 and \
                mouse_movement[0] <= 420 and mouse_movement[1] >= 50:#координаты нахождения очистить все
            clear()
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 460 and mouse_movement[1] <= 70 and \
                mouse_movement[
                    0] <= 480 and mouse_movement[1] >= 50:#координаты нахождения стерки
            color = 'white'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 520 and mouse_movement[1] <= 70 and \
                mouse_movement[
                    0] <= 540 and mouse_movement[1] >= 50:#координаты нахождения желтого цвета
            color = 'yellow'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 580 and mouse_movement[1] <= 70 and \
                mouse_movement[
                    0] <= 600 and mouse_movement[1] >= 50:#координаты нахождения зеленого цвета
            color = 'green'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 640 and mouse_movement[1] <= 70 and \
                mouse_movement[
                    0] <= 660 and mouse_movement[1] >= 50:#координаты нахождения синего цвета
            color = 'blue'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 700 and mouse_movement[1] <= 70 and \
                mouse_movement[
                    0] <= 720 and mouse_movement[1] >= 50:#координаты нахождения Красного цвета
            color = 'red'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 340 and mouse_movement[1] <= 70 and \
                mouse_movement[0] <= 360 and mouse_movement[1] >= 50:#координаты нахождения черного цвета
            color = 'black'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 260 and mouse_movement[1] <= 70 and \
                mouse_movement[0] <= 300 and mouse_movement[1] >= 30:#координаты нахождения круга
            mode = 'circle'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 220 and mouse_movement[1] <= 70 and \
                mouse_movement[0] <= 240 and mouse_movement[1] >= 50:#координаты нахождения квадрата
            mode = 'sq'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 110 and mouse_movement[1] <= 70 and \
                mouse_movement[0] <= 140 and mouse_movement[1] >= 40:#координаты нахождения прямого треугольника
            mode = 'right_triangle'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 65 and mouse_movement[1] <= 65 and \
                mouse_movement[0] <= 95 and mouse_movement[1] >= 40:#координаты нахождения равностороннего треугольника
            mode = 'equilateral_triangle'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 30 and mouse_movement[1] <= 65 and \
                mouse_movement[0] <= 40 and mouse_movement[1] >= 45:#координаты нахождения прямоугольника
            mode = 'rect'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 160 and mouse_movement[1] <= 80 and \
               mouse_movement[0] <= 200 and mouse_movement[1] >= 40:#координаты нахождения ромба
           mode = 'rhombus'
        if event.type == pygame.MOUSEBUTTONDOWN:#нажатие мышки
            drawing = True
            prev = mouse_movement
            start_pos = mouse_movement
        if event.type == pygame.MOUSEBUTTONUP:#отпущение мышки
            drawing = False
            end_pos = mouse_movement
            if mode == 'rect':#если выбрали прямоугольник
                rect(screen, color, start_pos, end_pos)
            elif mode == 'circle':#если выбрали круг
                circle(screen, color, start_pos, end_pos)
            elif mode == 'right_triangle':#если выбрали прямоугольный треугольник
                right_triangle(screen, color, start_pos, end_pos)
            elif mode == 'equilateral_triangle':#если выбрали равносторонний треугольник
                equilateral_triangle(screen, color, start_pos, end_pos)
            elif mode == 'rhombus':#если выбрали ромб
                rhombus(screen, color, start_pos, end_pos)
            elif mode == 'sq':#если выбрали квадрат
                 sq(screen, color,start_pos, end_pos)
        if event.type == pygame.MOUSEMOTION and drawing and mode == 'pen':#движение мышки
            cur = pygame.mouse.get_pos()
            if prev:
                pygame.draw.line(screen, color, prev, cur, 5)
                prev = cur

        pygame.draw.line(screen, 'beige', (750, 60), (725, 60), 30)#наша ручка
        pygame.draw.rect(screen, 'red', (700, 50, 20, 20))#красный цвет
        pygame.draw.rect(screen, 'blue', (640, 50, 20, 20))#синий цвет
        pygame.draw.rect(screen, 'green', (580, 50, 20, 20))#зеленый цвет
        pygame.draw.rect(screen, 'yellow', (520, 50, 20, 20))#желтый цвет
        pygame.draw.rect(screen, 'alice blue', (460, 50, 20, 20))#стерка
        pygame.draw.rect(screen, 'lavender', (400, 50, 20, 20))#очистить все
        pygame.draw.rect(screen, 'black', (340, 50, 20, 20))#черный цвет
        pygame.draw.circle(screen, 'beige', (280, 50), 20)#круг
        pygame.draw.rect(screen, 'beige', (220, 50, 20, 20))#квадрат
        pygame.draw.lines(screen, 'beige', True, ((180, 80), (160, 60), (180, 40), (200, 60)), 8)#ромб
        pygame.draw.polygon(screen, 'beige', ((110, 40), (110, 70), (140, 70)))#прямоугольный треугольник
        pygame.draw.polygon(screen, 'beige', ((65, 50), (95, 65), (80, 40)))#равносторонний треугольник
        pygame.draw.rect(screen, 'beige', (30, 45, 10, 20))#прямоугольник


    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()