import pygame

pygame.init()
Width, Height = 720, 720
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
    print(x1, x2, y1, y2)


def rect(screen, color, start, end):#рисование прямоугольника

    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    widthr = abs(x1 - x2)
    height = abs(y1 - y2)
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, color, (x1, y1, widthr, height), 3)
    if y2 > y1 and x1 > x2:
       pygame.draw.rect(screen, color, (x2, y1, widthr, height), 3)
    if x1 > x2 and y1 > y2:
       pygame.draw.rect(screen, color, (x2, y2, widthr, height), 3)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, color, (x1, y2, widthr, height), 3)


while game_over:
    mouse_movement = pygame.mouse.get_pos()
    print(mouse_movement)
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
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 30 and mouse_movement[1] <= 65 and \
                mouse_movement[0] <= 40 and mouse_movement[1] >= 45:#координаты нахождения прямоугольника
            mode = 'rect'
        if event.type == pygame.MOUSEBUTTONDOWN:#нажатие мышки
            drawing = True
            prev = mouse_movement
            start_pos = mouse_movement
        if event.type == pygame.MOUSEBUTTONUP:#отпущение мышку
            drawing = False
            end_pos = mouse_movement
            if mode == 'rect':
                rect(screen, color, start_pos, end_pos)
            elif mode == 'circle':
                circle(screen, color, start_pos, end_pos)
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
        pygame.draw.rect(screen, 'beige', (30, 45, 20, 40))#прямоугольник
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
