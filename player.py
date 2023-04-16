import pygame


class Player:
    def __init__(self, screen, player, x, y, step):
        self.screen = screen
        self.player = pygame.image.load(player)
        self.x = x
        self.y = y
        self.step = step

    def update(self):
        player_rect = self.player.get_rect(center=(self.x, self.y))

        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_d]:
            self.x += 5
        if key_input[pygame.K_a]:
            self.x -= 5

        player_rect.move(self.x, self.y)
        self.screen.blit(self.player, (self.x, self.y))
