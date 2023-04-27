import pygame
import math
import player1
import player2
import bullet1

pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("STARSTRA")
dt = clock.tick(30) / 1000

purple = (168, 103, 205)
green = (87, 147, 50)
white = (200, 200, 200)

bg = pygame.image.load("assets/background.jpg").convert()
bg_width = bg.get_width()

left_player = player1.Player1(screen, "assets/player1.png", 10, 460, 30, dt)
right_player = player2.Player2(screen, "assets/player2.png", 930, 460, 30, dt)

bullet_group_left = pygame.sprite.Group()
bullet_group_right = pygame.sprite.Group()
bulletCooldown1 = 0
bulletCooldown2 = 0

# Define game variables
scroll = 0
tiles = math.ceil(screen_width / bg_width) + 1

while True:
    # Draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    # Scroll background
    scroll -= 5

    # Reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    left_player.wall_collision()
    left_player.update()
    right_player.wall_collision()
    right_player.update()
    # Fire bullets when space bar is pressed
    if bulletCooldown1 == 0:
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LALT]:
            bulletCooldown1 += 20
            left_bullet = bullet1.Bullet1(
                screen,
                left_player.returnX(),
                left_player.returnY(),
                200,
                "assets/bullet1.png",
                dt,
            )
            bullet_group_left.add(left_bullet)
    else:
        bulletCooldown1 -= 1

    if bulletCooldown2 == 0:
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_RALT]:
            bulletCooldown2 += 20
            right_bullet = bullet1.Bullet1(
                screen,
                right_player.returnX(),
                right_player.returnY(),
                -200,
                "assets/bullet2.png",
                dt,
            )
            bullet_group_left.add(right_bullet)
    else:
        bulletCooldown2 -= 1

    bullet_group_left.draw(screen)
    bullet_group_left.update()
    bullet_group_right.draw(screen)
    bullet_group_right.update()
    clock.tick(30)
    pygame.display.update()
