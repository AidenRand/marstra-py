import pygame


class Bullet:
    def __init__(self, screen, color, width, height, x, y, y_speed):
        self.screen = screen
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.y_speed = y_speed
        self.bullet = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_bullet(self, fire_bullet):
        if fire_bullet:
            self.bullet.y -= self.y_speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.bullet)
