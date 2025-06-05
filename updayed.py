import pygame
import sys

pygame.init()

bg = pygame.image.load('background.jpg')
sprite = pygame.image.load('car.png')

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Adding text and images to window')

font = pygame.font.SysFont('Arial', 40, bold=True)
text = font.render('This is a Car', True, (0, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg, (0, 0))

    car_rect = sprite.get_rect(center=(width//2, height//2 - 50))
    screen.blit(sprite, car_rect)
    txt_rect = text.get_rect(center=(width//2, height//2 + 150))
    screen.blit(text, txt_rect)
    pygame.display.update()
