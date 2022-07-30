import pygame
import button
from saveloadmanager import SaveLoadSystem

pygame.init()  # Stop errors
pygame.font.init()  # For text


# Screen info
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pointless Clicking Game")  # Game title


# Loading buttons/images
shop_img = pygame.image.load('images/buttons/shop.png').convert_alpha()
cookie_img = pygame.image.load('images/buttons/cookie.png').convert_alpha()
reset_img = pygame.image.load('images/buttons/reset.png').convert_alpha()
menu_background_img = pygame.image.load('images/backgrounds/menu_background.png').convert_alpha()
pause_img = pygame.image.load('images/buttons/pause.png').convert_alpha()
pause_background_img = pygame.image.load('images/backgrounds/pause_background.png').convert_alpha()
game_background_img = pygame.image.load('images/backgrounds/game_background.png').convert_alpha()
shop_grandma_img = pygame.image.load('images/buttons/shop_grandma.png').convert_alpha()
shop_grandma_img_grey = pygame.image.load('images/buttons/shop_grandma_grey.png').convert_alpha()
shop_bakery_img = pygame.image.load('images/buttons/shop_bakery.png').convert_alpha()
shop_bakery_img_grey = pygame.image.load('images/buttons/shop_bakery_grey.png').convert_alpha()
shop_factory_img = pygame.image.load('images/buttons/shop_factory.png').convert_alpha()
shop_factory_img_grey = pygame.image.load('images/buttons/shop_factory_grey.png').convert_alpha()
close_img = pygame.image.load('images/buttons/close.png').convert_alpha()


# Create button instance
shop_button = button.Button(10, 10, shop_img, 1)
cookie_button = button.Cookie(SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/2 - 150, cookie_img, 0.75, 0)
reset_button = button.Button(150, 10, reset_img, 1)
menu_background = button.Button(0, 0, menu_background_img, 1)
pause_button = button.Button(740, 10, pause_img, 0.75)
pause_background = button.Button(0, 0, pause_background_img, 1)
game_background = button.Button(0, 0, game_background_img, 1)
shop_grandma_button = button.Cookie(100, 190, shop_grandma_img, 1, 0)
shop_grandma_button_grey = button.Cookie(100, 190, shop_grandma_img_grey, 1, 0)
shop_bakery_button = button.Cookie(100, 340, shop_bakery_img, 1, 0)
shop_bakery_button_grey = button.Cookie(100, 340, shop_bakery_img_grey, 1, 0)
shop_factory_button = button.Cookie(100, 490, shop_factory_img, 1, 0)
shop_factory_button_grey = button.Cookie(100, 490, shop_factory_img_grey, 1, 0)
close_button = button.Button(15, 15, close_img, 0.5)


# Text
current_score_font = pygame.font.SysFont('roboto', 50)  # Current cookies text
score_second_font = pygame.font.SysFont('roboto', 30)  # Cookies/s text
menu_title_font = pygame.font.SysFont('roboto', 70)  # Menu title
main_menu_font = pygame.font.SysFont('roboto', 35)  # Menu text
watermark_font = pygame.font.SysFont('roboto', 25)  # Menu watermark
shop_item_count_font = pygame.font.SysFont('roboto', 30)  # Shop item count

# Save/Load system - Default = 0 if no save file
saveloadmanager = SaveLoadSystem(".save", "save_data")
cookie_button.count = saveloadmanager.load_game_data(["cookies"], [0])  # Load saved cookies
cookie_button.grandma_count = saveloadmanager.load_game_data(["grandmas"], [0])  # Load saved grandmas
cookie_button.bakery_count = saveloadmanager.load_game_data(["bakeries"], [0])  # Load saved grandmas
cookie_button.factory_count = saveloadmanager.load_game_data(["factories"], [0])  # Load saved grandmas
cookie_button.cookies_per_click = saveloadmanager.load_game_data(["cookiesperclick"], [0])  # Load cookies/click


# Updating game display
def draw_window():
    game_background.draw(screen)

    # Button event logic
    # Screen is needed as an argument due to button being imported from another file
    if shop_button.draw(screen):  # When clicking shop button
        shop()
    if cookie_button.draw(screen):  # When clicking cookie button
        cookie_button.increasecount()
    if reset_button.draw(screen):  # When clicking reset button
        # cookie_button.count = saveloadmanager.delete_game_data("cookies")
        cookie_button.grandma_count = 0
    if pause_button.draw(screen):
        pause()

    # Showing cookie count / per click / shop items count
    current_cookie_text = current_score_font.render("Cookies: " + str(cookie_button.count), True, (255, 255, 255))
    screen.blit(current_cookie_text, (SCREEN_WIDTH / 50, SCREEN_HEIGHT - 115))
    cookie_per_click = score_second_font.render("Cookies Per Click: " + str(cookie_button.cookies_per_click), True, (255, 255, 255))
    screen.blit(cookie_per_click, (SCREEN_WIDTH / 50, SCREEN_HEIGHT - 50))
    current_grandma_count = shop_item_count_font.render("Grandmas: " + str(cookie_button.grandma_count), True, (255, 255, 255))
    screen.blit(current_grandma_count, (650, SCREEN_HEIGHT - 115))
    current_bakery_count = shop_item_count_font.render("Bakeries: " + str(cookie_button.bakery_count), True, (255, 255, 255))
    screen.blit(current_bakery_count, (650, SCREEN_HEIGHT - 85))
    current_factory_count = shop_item_count_font.render("Factories: " + str(cookie_button.factory_count), True, (255, 255, 255))
    screen.blit(current_factory_count, (650, SCREEN_HEIGHT - 55))

    pygame.draw.rect(screen, (0, 240, 0), (80, 10, 60, 60))  # Placeholder
    # pygame.draw.rect(screen, (240, 0, 0), (150, 10, 120, 60))  # Placeholder for reset

    pygame.display.update()


# Launching game window
if __name__ == "__main__":

    # Main menu
    def main_menu():
        clock = pygame.time.Clock()
        running = True

        # Menu loop
        while running:
            # Setting max FPS to 60
            clock.tick(60)

            menu_background.draw(screen)

            # Menu title
            main_menu_title = menu_title_font.render("POINTLESS CLICKING GAME", True, (255, 255, 255))
            screen.blit(main_menu_title, (SCREEN_WIDTH / 2 - 350, SCREEN_HEIGHT / 2 - 50))

            # Menu text
            main_menu_text = main_menu_font.render("Click anywhere to start!", True, (255, 255, 255))
            screen.blit(main_menu_text, (SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 + 75))

            # Menu watermark
            watermark_text = watermark_font.render("Aidan Gregory", True, (255, 255, 255))
            screen.blit(watermark_text, (SCREEN_WIDTH / 2 - 70, SCREEN_HEIGHT - 40))

            # Proceed events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Save current cookie count on exit
                    saveloadmanager.save_game_data([cookie_button.count], ["cookies"])
                    saveloadmanager.save_game_data([cookie_button.grandma_count], ["grandmas"])
                    saveloadmanager.save_game_data([cookie_button.bakery_count], ["bakeries"])
                    saveloadmanager.save_game_data([cookie_button.factory_count], ["factories"])
                    saveloadmanager.save_game_data([cookie_button.cookies_per_click], ["cookiesperclick"])
                    pygame.quit()
                    quit()

                # Start game when clicking in menu
                if event.type == pygame.MOUSEBUTTONDOWN:
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
                    saveloadmanager.save_game_data([cookie_button.grandma_count], ["grandmas"])
                    saveloadmanager.save_game_data([cookie_button.bakery_count], ["bakeries"])
                    saveloadmanager.save_game_data([cookie_button.factory_count], ["factories"])
                    saveloadmanager.save_game_data([cookie_button.cookies_per_click], ["cookiesperclick"])
                    pygame.quit()
                    quit()

            # Rendering items on screen
            draw_window()

    # Pause menu
    def pause():
        clock = pygame.time.Clock()
        running = True

        # Pause loop
        while running:
            # Setting max FPS to 60
            clock.tick(60)

            pause_background.draw(screen)

            # Menu title
            pause_menu_title = menu_title_font.render("PAUSED", True, (255, 255, 255))
            screen.blit(pause_menu_title, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50))

            # Menu text
            main_menu_text = main_menu_font.render("Click anywhere to resume!", True, (255, 255, 255))
            screen.blit(main_menu_text, (SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 + 75))

            # Proceed events
            for event in pygame.event.get():
                # Exit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Start game when clicking in menu
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game()

            # Rendering items on screen
            pygame.display.update()

    # Shop menu
    def shop():
        clock = pygame.time.Clock()
        running = True

        # Shop loop
        while running:
            # Setting max FPS to 60
            clock.tick(60)

            screen.fill((77, 77, 77))

            # Menu title
            shop_menu_title = menu_title_font.render("SHOP", True, (255, 255, 255))
            screen.blit(shop_menu_title, (SCREEN_WIDTH / 2 - 75, 50))

            current_cookie_text = current_score_font.render("Cookies: " + str(cookie_button.count), True, (255, 255, 255))
            screen.blit(current_cookie_text, (SCREEN_WIDTH / 50, SCREEN_HEIGHT - 150))

            # Shop item images + text

            # Grandma locked
            if cookie_button.count < 100:
                if shop_grandma_button_grey.draw(screen):
                    print("NOT ENOUGH COOKIES")
                grandma_item_text = main_menu_font.render("Grandma! (100 Cookies Required!)", True, (255, 255, 255))
                screen.blit(grandma_item_text, (SCREEN_WIDTH / 2 - 125, 240))
            # Grandma unlocked
            else:
                if shop_grandma_button.draw(screen):
                    cookie_button.grandma_count += 1
                    cookie_button.count -= 100
                    print("Grandma count = " + str(cookie_button.grandma_count))
                grandma_item_text = main_menu_font.render("Grandma! (2 Cookies per click)", True, (255, 255, 255))
                screen.blit(grandma_item_text, (SCREEN_WIDTH / 2 - 125, 240))

            # Bakery locked
            if cookie_button.count < 25:
                if shop_bakery_button_grey.draw(screen):
                    print("NOT ENOUGH COOKIES")
                bakery_item_text = main_menu_font.render("Bakery! (250 Cookies Required!)", True, (255, 255, 255))
                screen.blit(bakery_item_text, (SCREEN_WIDTH / 2 - 125, 400))
            # Bakery unlocked
            else:
                if shop_bakery_button.draw(screen):
                    cookie_button.bakery_count += 1
                    cookie_button.count -= 250
                    print("Bakery count = " + str(cookie_button.bakery_count))
                bakery_item_text = main_menu_font.render("Bakery! (5 Cookies per click)", True, (255, 255, 255))
                screen.blit(bakery_item_text, (SCREEN_WIDTH / 2 - 125, 400))

            # Factory locked
            if cookie_button.count < 25:
                if shop_factory_button_grey.draw(screen):
                    print("NOT ENOUGH COOKIES")
                factory_item_text = main_menu_font.render("Factory! (500 Cookies Required!)", True, (255, 255, 255))
                screen.blit(factory_item_text, (SCREEN_WIDTH / 2 - 125, 550))
            # Factory unlocked
            else:
                if shop_factory_button.draw(screen):
                    cookie_button.factory_count += 1
                    cookie_button.count -= 500
                    print("Factory count = " + str(cookie_button.factory_count))
                factory_item_text = main_menu_font.render("Factory! (10 Cookies per click)", True, (255, 255, 255))
                screen.blit(factory_item_text, (SCREEN_WIDTH / 2 - 125, 550))

            # Close menu button
            if close_button.draw(screen):
                game()

            # Proceed events
            for event in pygame.event.get():
                # Exit game
                if event.type == pygame.QUIT:
                    # Save current cookie count on exit
                    saveloadmanager.save_game_data([cookie_button.count], ["cookies"])
                    saveloadmanager.save_game_data([cookie_button.grandma_count], ["grandmas"])
                    saveloadmanager.save_game_data([cookie_button.bakery_count], ["bakeries"])
                    saveloadmanager.save_game_data([cookie_button.factory_count], ["factories"])
                    saveloadmanager.save_game_data([cookie_button.cookies_per_click], ["cookiesperclick"])
                    pygame.quit()
                    quit()

            # Rendering items on screen
            pygame.display.update()


    main_menu()
