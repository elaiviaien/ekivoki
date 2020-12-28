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
    pygame.display.flip()


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
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
    font = pygame.font.Font(None, 32)
    game = True
    button = Button(100, 50)
    start_button = Button(1000, 50)
    input_box = pygame.Rect(50, 50, 140, 32)
    input_box_player = pygame.Rect(400, 50, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    color_pl = color_inactive
    active_p = False
    active = False
    text = ''
    text_p = ''
    players =''
    player = []
    player_point = {}
    done = False
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active_p = not active_p
                else:
                    active_p = False
                color = color_active if active_p else color_inactive
                if input_box_player.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color_pl = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active_p:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text_p = text_p[:-1]
                    else:
                        text_p += event.unicode
                    if event.key == pygame.K_RETURN:
                        if text_p not in player:
                            player.append(text_p)
                            player_point = {point: 0 for point in player}

            if text:
                win_points = int(text)
                print(win_points)
            print(player)
            print(player_point)
        clock.tick(60)
        display.blit(bg, (0, 0))
        txt_surface = font.render(text, True, color)
        txt_surface_p = font.render(text_p, True, color)
        txt_points = font.render('Очки для победы', True, color)
        txt_players = font.render('Добавить иигрока', True, color_pl)
        txt_player_name = font.render('Игроки:', True, pygame.Color('white'))

        for i in player:
            if i not in players.split():
                players += i
                players +=' '
        txt_players_list = font.render(players, True, pygame.Color('white'))

        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        display.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        display.blit(txt_points, (50, 30))
        start_button.draw(0, 650, 'Начать игру')
        pygame.draw.rect(display, color, input_box, 2)
        display.blit(txt_surface_p, (input_box_player.x + 5, input_box_player.y + 5))
        display.blit(txt_players, (400, 30))
        display.blit(txt_player_name, (10, 200))
        display.blit(txt_players_list, (100, 200))
        pygame.draw.rect(display, color_pl, input_box_player, 2)

        pygame.display.flip()
        clock.tick(30)


menu()
