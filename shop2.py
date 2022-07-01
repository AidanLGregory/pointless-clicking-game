import pygame

pygame.init()
pygame.font.init()  # For text

font = pygame.font.SysFont('', 30)


class Shop(pygame.sprite.Sprite):

    def __init__(self):
        super(Shop, self).__init__()

        self.cookie_count = 0
        self.grandma_count = 0
        self.cookies_per_second = 0

        self.grandma = 10  # grandma bakes 10 cookies/second

        text = font.render("Cookies: " + str(self.cookie_count), True, (255,0,0), (0,0,0))
        self.image = text

        # self.rect = self.image.get_rect(topleft=position)

    def update_grandma_count(self):
        self.grandma_count += 1

    def update_cookies(self):
        if self.grandma_count > 0:
            self.cookie_count += self.grandma * self.grandma_count  # 10 cookies per grandma
            if self.cookie_count > 1000:
                self.cookie_count = 0
            text = font.render("Cookies: " + str(self.cookie_count), True, (255,0,0), (0,0,0))
            self.image = text
