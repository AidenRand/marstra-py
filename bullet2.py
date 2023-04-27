import pygame


class Bullet2(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, y_speed, image, dt):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y
        self.y_speed = y_speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.dt = dt

    def update(self):
        self.rect.x += self.y_speed * self.dt
        if self.rect.left < 0:
            self.kill()
