import pygame
import player
import bullet

pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("STARSTRA")


purple = (168, 103, 205)
green = (87, 147, 50)
white = (200, 200, 200)

x = 460
y = 700
new_player = player.Player(screen, "assets/player.png", x, y, 7)

bullet_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((5, 5, 5))
    new_player.wall_collision()
    new_player.update()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_SPACE]:
        new_bullet = bullet.Bullet(screen, x, y, 10)
        bullet_group.add(new_bullet)
    bullet_group.draw(screen)
    bullet_group.update()
    clock.tick(30)
    pygame.display.flip()
