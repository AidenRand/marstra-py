import pygame


class Player:
    def __init__(self, screen, player, x, y, step):
        self.screen = screen
        self.player = pygame.image.load(player)
        self.x = x
        self.y = y
        self.player_rect = self.player.get_rect(center=(self.x, self.y))
        self.step = step

    def update(self):
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_d]:
            self.x += self.step
        if key_input[pygame.K_a]:
            self.x -= self.step

        if self.x >= 960:
            self.x -= self.step
        if self.x <= 0:
            self.x += self.step

        self.player_rect.move(self.x, self.y)
        self.screen.blit(self.player, (self.x, self.y))

    def wall_collision(self):
        if self.player_rect.right >= 950:
            self.x -= 10
        if self.player_rect.left <= 10:
            self.x += 10
