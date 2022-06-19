import pygame
import button
from saveloadmanager import SaveLoadSystem

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
cookie_button = button.Cookie(SCREEN_WIDTH/2 - 60, SCREEN_HEIGHT/2 - 60, cookie_img, 1, 0)  # TODO fix button img


# Variables
score_font = pygame.font.SysFont('roboto', 50)
saveloadmanager = SaveLoadSystem(".save", "save_data")
# cookie_button.count = saveloadmanager.load_data("cookies")
cookie_button.count = saveloadmanager.load_game_data(["cookies"], [[]])  # Loading saved cookie count, and blank if default


# Updating game display
def draw_window():
    screen.fill((37, 150, 207))

    # pygame.draw.rect(screen, (0, 0, 0), (10, 10, 60, 60))  # Placeholder for shop

    # Button event logic
    # Screen is needed as an argument due to button being imported from another file
    if shop_button.draw(screen):  # When clicking on shop button
        print("SHOP")
    if cookie_button.draw(screen):  # When clicking on cookie button
        # Increases score
        cookie_button.increasecount()
        print(cookie_button.count)

    # Showing cookie count
    current_score_text = score_font.render("Cookies: " + str(cookie_button.count), 1, (255, 255, 255))
    screen.blit(current_score_text, (SCREEN_WIDTH / 50, SCREEN_HEIGHT - 50))

    pygame.draw.rect(screen, (0, 240, 0), (80, 10, 60, 60))  # Placeholder for cookie
    pygame.draw.rect(screen, (240, 0, 0), (150, 10, 60, 60))  # Placeholder for Pause

    pygame.display.update()


# Launching game window
if __name__ == "__main__":

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
                # Save current cookie count on exit
                # saveloadmanager.save_data(cookie_button.count, "cookies")
                saveloadmanager.save_game_data([cookie_button.count], ["cookies"])
                pygame.quit()
                quit()

            # Increase score on left click
            # if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # current_score += 1  # TODO change to only increase score when clicking on item

        # Rendering items on screen
        draw_window()
