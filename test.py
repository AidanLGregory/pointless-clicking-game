import pygame

height = 500
width = 800

screen = pygame.display.set_mode((width, height))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
