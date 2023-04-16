import pygame
import player

pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("STARSTRA")

purple = (168, 103, 205)
green = (87, 147, 50)
white = (200, 200, 200)


new_player = player.Player(screen, "assets/pixil-frame-0(6).png", 460, 650, 5)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((5, 5, 5))
    new_player.update()
    clock.tick(60)
    pygame.display.flip()
