import pygame


class Bullet2(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, y_speed, image):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y
        self.y_speed = y_speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.x += self.y_speed
        if self.rect.left > 1000:
            self.kill()
