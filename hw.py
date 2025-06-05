import pygame
import sys

pygame.init()

og_sprite = pygame.image.load('car.png')
sprite = pygame.transform.scale(og_sprite, (300, 300))

l, b = 500, 500
screen = pygame.display.set_mode((l, b))
pygame.display.set_caption('My first game screen')

GREY = (128, 128, 128)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(GREY)

    sprite_rect = sprite.get_rect(center=(l//2, b//2))
    screen.blit(sprite, sprite_rect)
    pygame.display.update()
