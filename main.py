import pygame

pygame.init()

width = 1000
height = 700

display= pygame.display.set_mode((width,height))

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

def run_game():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.fill((255,255,255))
        pygame.display.update()
run_game()