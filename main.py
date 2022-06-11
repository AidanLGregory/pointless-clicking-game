import pygame
import sys

pygame.font.init()  # For text

# TODO make OOP
# class Setting:
#
#     def __init__(self, width, height):
#         # Game window
#         self.width = width
#         self.height = height
#         self.color = (255, 255, 255)
#
#         self.screen = pygame.display.set_mode((self.width, self.height))
#
#         pygame.display.set_caption("Pointless Clicking Game")
#
#
# class Box(pygame.sprite.Sprite):
#
#     def __init__(self, setting):
#         super().__init__()
#
#         self.setting = setting
#
#

width, height = 800, 800
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Pointless Clicking Game")


# Variables
score_font = pygame.font.SysFont('roboto', 75)


# Updating game display
def draw_window(current_score):
    # Have to fill background first, as order matters
    screen.fill((37, 150, 207))

    # Drawing fonts for score
    current_score_text = score_font.render("Current Score: " + str(current_score), 1, (255, 255, 255))
    # screen.blit(current_score_text, (width - current_score_text.get_width() - 10, 10))
    screen.blit(current_score_text, (width/2 - current_score_text.get_width() + 200, height/2 - 50))

    pygame.display.update()


# Launching game window
def main():
    pygame.init()
    clock = pygame.time.Clock()

    running = True
    current_score = 0

    # Running game
    while running:
        # Setting max FPS to 60
        clock.tick(60)

        # Proceed events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # TODO check if needed
                pygame.quit()
                sys.exit()

            # Increase score on left click
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                current_score += 1

        # Rendering items on screen
        draw_window(current_score)

    # Rerun game when someone wins
    main()


# Run game when this file runs
if __name__ == "__main__":
    main()
