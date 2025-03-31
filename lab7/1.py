import pygame
from datetime import datetime

pygame.init()
pygame.display.set_caption('Mickey_Clock')
WIDTH, HEIGHT = 800, 800
FPS = 45

screen = pygame.display.set_mode((WIDTH, HEIGHT))
center = WIDTH//2, HEIGHT//2
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load('C:\programmingFORbss\pp2\pp2-21B030328\lab7\images\mickey_clock.jpg'), (800, 800))
left_hand = pygame.transform.scale(pygame.image.load('C:\programmingFORbss\pp2\pp2-21B030328\lab7\images\left hand.png'), (385, 115))
right_hand = pygame.transform.scale(pygame.image.load('C:\programmingFORbss\pp2\pp2-21B030328\lab7\images\mright hand.png'), (297, 161))

def blitRotate(screen, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0]- originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    screen.blit(rotated_image, rotated_image_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    current_time = datetime.now()
    second = current_time.second
    minute = current_time.minute

    theta = (minute + second / 60) * (360 / 60)
    blitRotate(screen, right_hand, center, (right_hand.get_width() / 2 + 110, left_hand.get_height() / 2 + 75), theta + 75)

    theta = (second + minute * 60) * (360 / 60)
    blitRotate(screen, left_hand, center, (left_hand.get_width() / 2 - 145, left_hand.get_height() / 2), theta - 87)
    pygame.display.flip()
pygame.quit()