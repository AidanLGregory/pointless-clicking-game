import pygame

pygame.init()
pygame.font.init()  # For text


SIZE = WIDTH, HEIGHT = 800, 800
FPS = 60
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BACKGROUND_COLOR = pygame.Color('white')

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
font = pygame.font.SysFont('', 30)

COOKIE_EVENT = pygame.USEREVENT
pygame.time.set_timer(COOKIE_EVENT, 1000)  # periodically create COOKIE_EVENT


class Player(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Player, self).__init__()

        self.cookie_count = 0
        self.grandma_count = 2
        self.cookies_per_second = 0

        self.grandma = 10  # grandma bakes 10 cookies/second

        text = font.render("Cookies: " + str(self.cookie_count), True, RED, BLACK)
        self.image = text

        self.rect = self.image.get_rect(topleft=position)

    def update_grandma_count(self):
        self.grandma_count += 1

    def update_cookies(self):
        if self.grandma_count > 0:
            self.cookie_count += self.grandma * self.grandma_count  # 10 cookies per grandma
            if self.cookie_count > 1000:
                self.cookie_count = 0
            text = font.render("Cookies: " + str(self.cookie_count), True, RED, BLACK)
            self.image = text


player = Player(position=(350, 220))

running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == COOKIE_EVENT:
            player.update_cookies()

    screen.fill(BACKGROUND_COLOR)
    screen.blit(player.image, player.rect)

    pygame.display.update()

# import pygame
# import button
#
# pygame.init()
# pygame.font.init()  # For text
#
# screen = pygame.display.set_mode((800, 600)) # change to the real resolution
#
# shop_img = pygame.image.load('images/buttons/shop.png').convert_alpha()
# shop_button = button.Button(10, 10, shop_img, 1)
#
# BLACK = (0,0,0)
# WHITE = (255,255,255)
# GREEN = (0,255,0)
# RED = (255,0,0)
#
# font = pygame.font.SysFont('roboto', 30)


