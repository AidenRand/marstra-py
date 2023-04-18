import pygame
import player
import bullet

pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("STARSTRA")

bg_img = pygame.image.load("assets/background.png")
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))


purple = (168, 103, 205)
green = (87, 147, 50)
white = (200, 200, 200)

x = 460
y = 700
new_player = player.Player(screen, "assets/player.png", x, y, 7)
new_bullet = bullet.Bullet(screen, white, 5, 10, x, y, 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((5, 5, 5))
    screen.blit(bg_img, (0, 0))
    new_player.wall_collision()
    new_player.update()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_SPACE]:
        new_bullet.move_bullet(True)
    new_bullet.draw_bullet()
    clock.tick(60)
    pygame.display.flip()
