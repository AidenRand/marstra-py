import pygame

pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("STARSTA")

purple = (168, 103, 205)
green = (87, 147, 50)
white = (200, 200, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((5, 5, 5))

    clock.tick(6)
    pygame.display.flip()
