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
reset_img = pygame.image.load('images/reset.png').convert_alpha()
menu_background_img = pygame.image.load('images/menu_background.png').convert_alpha()


# Create button instance
shop_button = button.Button(10, 10, shop_img, 1)
cookie_button = button.Cookie(SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/2 - 150, cookie_img, 0.75, 0)  # TODO fix button img
reset_button = button.Button(150, 10, reset_img, 1)
menu_background = button.Button(0, 0, menu_background_img, 1)

# Text
current_score_font = pygame.font.SysFont('roboto', 50)  # Current cookies text
score_second_font = pygame.font.SysFont('roboto', 30)  # Cookies/s text
main_menu_title_font = pygame.font.SysFont('roboto', 70)  # Menu title
main_menu_font = pygame.font.SysFont('roboto', 35)  # Menu text
watermark_font = pygame.font.SysFont('roboto', 25)  # Menu watermark

# Save/Load system
saveloadmanager = SaveLoadSystem(".save", "save_data")
cookie_button.count = saveloadmanager.load_game_data(["cookies"], [0])  # Load saved cookies if exists, or 0 cookies


# Updating game display
def draw_window():
    screen.fill((37, 150, 207))

    # pygame.draw.rect(screen, (0, 0, 0), (10, 10, 60, 60))  # Placeholder for shop

    # Button event logic
    # Screen is needed as an argument due to button being imported from another file
    if shop_button.draw(screen):  # When clicking shop button
        print("SHOP")
    if cookie_button.draw(screen):  # When clicking cookie button
        # Increases score
        cookie_button.increasecount()
    if reset_button.draw(screen):  # When clicking reset button
        cookie_button.count == 0

    # Showing cookie count
    current_score_text = current_score_font.render("Cookies: " + str(cookie_button.count), 1, (255, 255, 255))
    screen.blit(current_score_text, (SCREEN_WIDTH / 50, SCREEN_HEIGHT - 100))
    current_score_second = score_second_font.render("Cookies Per Second: " + str(0), 1, (255, 255, 255))
    screen.blit(current_score_second, (SCREEN_WIDTH / 50, SCREEN_HEIGHT - 50))

    pygame.draw.rect(screen, (0, 240, 0), (80, 10, 60, 60))  # Placeholder
    # pygame.draw.rect(screen, (240, 0, 0), (150, 10, 120, 60))  # Placeholder for reset

    pygame.display.update()


# Launching game window
if __name__ == "__main__":

    def main_menu():
        clock = pygame.time.Clock()
        running = True

        # Menu loop
        while running:
            # Setting max FPS to 60
            clock.tick(60)

            menu_background.draw(screen)

            # Menu title
            main_menu_title = main_menu_title_font.render("POINTLESS CLICKING GAME", 1, (255, 255, 255))
            screen.blit(main_menu_title, (SCREEN_WIDTH / 2 - 350, SCREEN_HEIGHT / 2 - 50))

            # Menu text
            main_menu_text = main_menu_font.render("Click anywhere to start!", 1, (255, 255, 255))
            screen.blit(main_menu_text, (SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 + 75))

            # Menu watermark
            watermark_text = watermark_font.render("Aidan Gregory", 1, (255, 255, 255))
            screen.blit(watermark_text, (SCREEN_WIDTH / 2 - 75, SCREEN_HEIGHT - 40))


            # Proceed events
            for event in pygame.event.get():
                # Exit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Start game when clicking in menu
                if event.type == pygame.MOUSEBUTTONUP:
                    game()

            # Rendering items on screen
            pygame.display.update()


    def game():
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
                    saveloadmanager.save_game_data([cookie_button.count], ["cookies"])
                    pygame.quit()
                    quit()

                # Increase score on left click
                # if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    # current_score += 1  # TODO change to only increase score when clicking on item

            # Rendering items on screen
            draw_window()


    main_menu()
