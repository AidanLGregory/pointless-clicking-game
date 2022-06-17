import pygame


# Button class
class Button:
    def __init__(self, x, y, image, scale):
        # Original width/height of image
        width = image.get_width()
        height = image.get_height()

        # Takes height/width of original image and then scales it
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

        # Allows for setting position based on co-ordinates
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.clicked = False  # To allow a single click

    # Draw button on screen
    def draw(self, surface):
        # Changes for each button
        action = False

        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouseover and clicked button
        if self.rect.collidepoint(pos):  # If hovering on button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:  # If left click + hovering
                self.clicked = True
                action = True

        # Reset clicked variable so that I can select button again
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action  # True/False
