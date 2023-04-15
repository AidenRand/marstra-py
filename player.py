import pygame


class Player:
    def __init__(self, screen, player, x, y):
        self.screen = screen
        self.player = pygame.image.load(player)
        self.x = x
        self.y = y

    def draw_player(self):
        self.screen.blit(self.player, (self.x, self.y))
