import pygame


class Player1:
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
        if key_input[pygame.K_w]:
            self.y -= self.step
        if key_input[pygame.K_s]:
            self.y += self.step

        self.player_rect.move(self.x, self.y)
        self.screen.blit(self.player, (self.x, self.y))

    def wall_collision(self):
        if self.x <= 0:
            self.x += self.step
        if self.x >= 260:
            self.x -= self.step
        if self.y >= 740:
            self.y -= self.step
        if self.y <= 0:
            self.y += self.step

    def returnX(self):
        return self.x + 32

    def returnY(self):
        return self.y + 32
