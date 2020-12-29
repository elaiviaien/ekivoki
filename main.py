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


def wait():
    pygame.event.clear()

    while True:
        mouse = pygame.mouse.get_pos()

        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN and 100 < mouse[0] < 100 + 215 and 100 < mouse[1] < 100 + 50:
            break


def print_text(message, x, y, font_color=(0, 0, 0), font_type='20051.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))
    pygame.display.update()


def win_screen(i):
    while True:
        display.blit(bg, (0, 0))
        txt_cong = font.render("Поздарвления!!!", True, pygame.Color('white'))
        display.blit(txt_cong, (200, 200))
        txt_name = font.render(f"{i} победил(а)", True, pygame.Color('white'))
        display.blit(txt_name, (200, 300))
        pygame.display.flip()


def game_menu():
    global player, font, game_s, player_point, win_points
    button = Button(215, 50)
    while True:
        for i in player:

            display.blit(bg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            button.draw(100, 100, 'Крутить кубик', lambda: draw_cube(i))
            wait()


            pygame.display.flip()


def draw_cube(i):
    global res,player_point
    f =None
    task = ''
    task_n = ''
    res = rnd.randrange(1, 7)
    txt_player_name = font.render(f'Игрок: {i}', True, pygame.Color('white'))
    filename = f'cube/{res}.png'
    playerStand = pygame.image.load(filename)
    display.blit(playerStand, (cube_x, cube_y))
    display.blit(txt_player_name, (10, 200))
    print(res)
    print(f'player: {i}')
    if res == 1:
        task_n += "Обьясни словами:"
        f = open("tasks/1.txt", "r", encoding="utf-8")
    elif res == 2:
        task_n += "Прочитай 3 раза наоборот:"
        f = open("tasks/2.txt", "r", encoding="utf-8")
    elif res == 3:
        task_n += "Нарисуй:"
        f = open("tasks/3.txt", "r", encoding="utf-8")
    elif res == 4:
        task_n += "Покажи жестами:"
        f = open("tasks/4.txt", "r", encoding="utf-8")
    elif res == 5:
        task_n += "Да/нет:"
        f = open("tasks/5.txt", "r", encoding="utf-8")
    elif res == 6:
        task= 'Ты не должен выполять задание'
    if f:
        task += f.read().split('\n')[rnd.randrange(1, 6)]
        f.close()
    player_point[i] += res
    if task_n:
        txt_task_n = font.render(task_n, True, pygame.Color('white'))
        display.blit(txt_task_n, (400, 30))

    txt_task = font.render(task, True, pygame.Color('white'))
    display.blit(txt_task, (400, 50))
    player_points_text = "Счет: "+str(player_point).replace("{","").replace("}","").replace("'","")
    txt_points = font.render(player_points_text, True, pygame.Color('white'))
    display.blit(txt_points, (0, 500))
    pygame.time.delay(100)
    pygame.display.flip()
    print(player_point)
    for key, value in player_point.items():
        if value not in range(win_points):
            win_screen(key)


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
    global res, player, font,player_point,win_points
    font = pygame.font.Font(None, 32)
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
    players = ''
    player = []
    player_point = {}
    while True:
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
                players += ' '
        txt_players_list = font.render(players, True, pygame.Color('white'))
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        display.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        display.blit(txt_points, (50, 30))
        start_button.draw(0, 650, 'Начать игру', lambda: game_menu())
        pygame.draw.rect(display, color, input_box, 2)
        display.blit(txt_surface_p, (input_box_player.x + 5, input_box_player.y + 5))
        display.blit(txt_players, (400, 30))
        display.blit(txt_player_name, (10, 200))
        display.blit(txt_players_list, (100, 200))
        pygame.draw.rect(display, color_pl, input_box_player, 2)
        pygame.display.flip()
        clock.tick(30)


menu()
