import pygame
import settings
pygame.init()
pygame.display.set_mode((500, 500))
pygame.display.set_caption('my_game')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(settings.FPS)