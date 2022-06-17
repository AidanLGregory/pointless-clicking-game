import pygame
import button

pygame.init()  # Stop errors
pygame.font.init()  # For text

# Screen info
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pointless Clicking Game")  # Game title

# Load button images
shop_img = pygame.image.load('images/shop.png').convert_alpha()
cookie_img = pygame.image.load('images/cookie.png').convert_alpha()

# Create button instance
shop_button = button.Button(10, 10, shop_img, 1)
cookie_button = button.Button(80, 10, cookie_img, 1)

# Variables
score_font = pygame.font.SysFont('roboto', 50)
current_score = 0


# Updating game display
def draw_window(current_score):
    screen.fill((37, 150, 207))

    # Drawing fonts for score
    # screen.blit(current_score_text, (width / 2 - current_score_text.get_width() + 200, height / 2 - 50))

    # pygame.draw.rect(screen, (0, 0, 0), (10, 10, 60, 60))  # Placeholder for shop

    if shop_button.draw(screen):  # When clicking on shop button, do this - screen is needed as an argument due to button being imported from another file
        print('SHOP')

    if cookie_button.draw(screen):
        # global current_score
        print("COOKIE")
        # current_score += 1

    current_score_text = score_font.render("Score: " + str(current_score), 1, (255, 255, 255))
    screen.blit(current_score_text, (SCREEN_WIDTH / 50, 750))

    # pygame.draw.rect(screen, (0, 240, 0), (80, 10, 60, 60))  # Placeholder for cookie
    pygame.draw.rect(screen, (240, 0, 0), (150, 10, 60, 60))  # Placeholder for Pause

    pygame.display.update()


# Launching game window
# def main():
clock = pygame.time.Clock()

running = True

# Game loop
while running:
    # Setting max FPS to 60
    clock.tick(60)


    # Proceed events
    for event in pygame.event.get():
        # Exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Increase score on left click
        # if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # current_score += 1  # TODO change to only increase score when clicking on item

    # Rendering items on screen
    draw_window(current_score)

# Run game when this file runs
# if __name__ == "__main__":
# TODO fix this
