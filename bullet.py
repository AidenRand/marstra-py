import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, y_speed):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y
        self.y_speed = y_speed
        self.image = pygame.image.load("assets/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= self.y_speed
