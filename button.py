import pygame


# Parent button class
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


# Child cookie button
class Cookie(Button):
    def __init__(self, x, y, image, scale, count):  # Taken from parent class + new attributes
        super().__init__(x, y, image, scale)  # Needed to use from parent class

        self.count = count

    def increasecount(self):
        # Increases score when clicking on cookie
        self.count += 1


# Child reset button
class Reset(Button):
    def __init__(self, x, y, image, scale, count):  # Taken from parent class + new attributes
        super().__init__(x, y, image, scale)  # Needed to use from parent class

        self.count = count

    def resetcount(self):
        # Reset score with click
        self.count += 1
