import pygame

pygame.init()

FPS = 20
clock = pygame.time.Clock()
x, y = 300, 300
screen = pygame.display.set_mode((600, 600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]: y -= 20
    if pressed[pygame.K_DOWN]: y += 20
    if pressed[pygame.K_LEFT]: x -= 20
    if pressed[pygame.K_RIGHT]: x += 20
    if x > 580: x -= 20
    if y > 580: y -= 20
    if x < 20: x += 20
    if y < 20: y += 20
    screen.fill('white')
    pygame.draw.circle(screen, 'red', (x, y), 25, 0)

    pygame.display.flip()
    clock.tick(FPS)