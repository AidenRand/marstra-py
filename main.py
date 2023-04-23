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

x = 60
y = 460
new_player = player.Player(screen, "assets/player1.png", x, y, 10)

bullet_group = pygame.sprite.Group()
bulletCooldown = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((5, 5, 5))
    new_player.wall_collision()
    new_player.update()
    # Fire bullets when space bar is pressed
    if bulletCooldown == 0:
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_SPACE]:
            bulletCooldown += 20
            new_bullet = bullet.Bullet(
                screen, new_player.returnX(), new_player.returnY(), 50
            )
            bullet_group.add(new_bullet)
    else:
        bulletCooldown -= 1

    bullet_group.draw(screen)
    bullet_group.update()
    clock.tick(30)
    pygame.display.flip()
