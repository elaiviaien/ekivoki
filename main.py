import pygame
import random as rnd

pygame.init()

width = 1000
height = 700
display = pygame.display.set_mode((width, height))

icon = pygame.image.load("icon.png")
bg = pygame.image.load('bg.png')

pygame.display.set_icon(icon)
cube_x = (width / 2) - (width / 2.2)
cube_y = (height / 2) - (height / 2.2)
clock = pygame.time.Clock()
res = 0
roll = True

def print_text(message, x, y, font_color=(0, 0, 0), font_type='20051.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))
    pygame.display.update()

def draw_cube():
    global res
    print("rerggdfg")
    res = rnd.randrange(1, 6)
    filename = f'{res}.png'
    playerStand = pygame.image.load(filename)
    display.blit(playerStand, (cube_x, cube_y))
    pygame.display.update()




class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and  y < mouse[1] < y + self.height :
            pygame.draw.rect(display, (23, 204, 58), (x, y, self.width, self.height))
            print_text(message, x + 10, y + 10)
            if click[0] == 1:
                if action is not None:
                    action()
                    pygame.time.delay(100)
        else:
            pygame.draw.rect(display, (14, 162, 58), (x, y, self.width, self.height))
            print_text(message, x + 10, y + 10)




def menu():
    global res
    game = True
    button = Button(100, 50)
    display.blit(bg, (0, 0))
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button.draw(20, 100, 'Крутить кубик',lambda :draw_cube())
        clock.tick(60)
menu()
