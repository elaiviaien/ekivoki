import pygame
import random as rnd

pygame.init()

width = 1000
height = 700
display = pygame.display.set_mode((width, height))

icon = pygame.image.load("icon.png")
bg = pygame.image.load('bg.png')
font = pygame.font.Font(None, 32)
pygame.display.set_icon(icon)
cube_x = (width / 2) - (width / 2.2)
cube_y = (height / 2) - (height / 2.2)
clock = pygame.time.Clock()
res = 0
roll = True
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')


def wait():
    pygame.event.clear()

    while True:
        mouse = pygame.mouse.get_pos()

        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN and (
                (100 < mouse[0] < 100 + 215 and 100 < mouse[1] < 100 + 50) or (400 < mouse[1] < 400 + 50)):
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
    button = Button(215, 50, 'Крутить кубик', lambda: draw_cube(i))
    while True:
        for i in player:

            display.blit(bg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            button.draw(100, 100)
            wait()

            pygame.display.flip()

def draw_cube(i):
    global res, player_point, player
    f = None
    task = ''
    task_n = ''
    text_p_a = ''

    input_box = InputBox(440, 390, 140, 32, None,None, text_p_a, None, None, None)
    txt_answer = font.render(f'Введите имя игрока который угадал:', True, pygame.Color('white'))
    display.blit(txt_answer, (0, 400))
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
        task = 'Ты не должен выполнять задание'
    if f:
        task += f.read().split('\n')[rnd.randrange(1, 6)]
        f.close()
    player_point[i] += res
    if task_n:
        txt_task_n = font.render(task_n, True, pygame.Color('white'))
        display.blit(txt_task_n, (400, 30))
    txt_task = font.render(task, True, pygame.Color('white'))
    display.blit(txt_task, (400, 50))
    pygame.event.clear()
    while True:
        event = pygame.event.wait()
        input_box.handle_event(event)
        input_box.update()
        input_box.draw(display)
        pygame.display.flip()
        clock.tick(10)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                break
    player_points_text = "Счет: " + str(player_point).replace("{", "").replace("}", "").replace("'", "")
    txt_points = font.render(player_points_text, True, pygame.Color('white'))
    display.blit(txt_points, (0, 500))
    pygame.time.delay(100)
    pygame.display.flip()
    print(player_point)
    for key, value in player_point.items():
        if value not in range(win_points):
            win_screen(key)


class Button:
    def __init__(self, width, height, message, action=None):
        self.width = width
        self.height = height
        self.message = message
        self.action = action

    def draw(self, x, y):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(display, (23, 204, 58), (x, y, self.width, self.height))
            print_text(self.message, x + 10, y + 10)
            if click[0] == 1:
                if self.action is not None:
                    self.action()
                    pygame.time.delay(100)
        else:
            pygame.draw.rect(display, (14, 162, 58), (x, y, self.width, self.height))
            print_text(self.message, x + 10, y + 10)


class InputBox:

    def __init__(self, x, y, w, h, text, text_p,text_p_a, players, player, player_point):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color_inactive
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        self.text_p = text_p
        self.players = players
        self.player = player
        self.player_point = player_point
        self.text_p_a =text_p_a
    def handle_event(self, event):
        global res, player, font, player_point, win_points
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = color_active if self.active else color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if self.text is not None:
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    self.txt_surface = font.render(self.text, True, self.color)
                if self.text_p is not None:
                    if event.key == pygame.K_BACKSPACE:
                        self.text_p = self.text_p[:-1]
                    else:
                        self.text_p += event.unicode
                    self.txt_surface = font.render(self.text_p, True, self.color)
                    if event.key == pygame.K_RETURN:
                        if self.text_p not in player:
                            player.append(self.text_p)
                            player_point = {point: 0 for point in player}
                if self.text_p_a is not None:
                    if event.key == pygame.K_BACKSPACE:
                        self.text_p_a = self.text_p_a[:-1]
                    else:
                        self.text_p_a += event.unicode
                    self.txt_surface = font.render(self.text_p_a, True, self.color)
                    if event.key == pygame.K_RETURN:
                        player_point[self.text_p_a] += res
        if self.text:
            win_points = int(self.text)
            print(win_points)

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


def menu():
    global res, player, font, player_point, win_points
    start_button = Button(1000, 50, 'Начать игру', lambda: game_menu())
    color = color_inactive
    color_pl = color_inactive
    text_p = ''
    text = ''
    players = ''
    player = []
    player_point = {}
    input_box1 = InputBox(50, 60, 140, 32, text, None, None, None,None,None)
    input_box_p = InputBox(400, 60, 140, 32, None, text_p,None, players, player, player_point)
    input_boxes = [input_box1, input_box_p]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            for box in input_boxes:
                box.handle_event(event)

            print(player)
            print(player_point)
        for box in input_boxes:
            box.update()
        for box in input_boxes:
            box.draw(display)

        pygame.display.flip()
        clock.tick(10)

        display.blit(bg, (0, 0))
        txt_points = font.render('Очки для победы', True, color)
        txt_players = font.render('Добавить игрока', True, color_pl)
        txt_player_name = font.render('Игроки:', True, pygame.Color('white'))

        for i in player:
            if i not in players.split():
                players += i
                players += ' '
        txt_players_list = font.render(players, True, pygame.Color('white'))
        display.blit(txt_points, (50, 30))
        start_button.draw(0, 650)
        display.blit(txt_players, (400, 30))
        display.blit(txt_player_name, (10, 200))
        display.blit(txt_players_list, (100, 200))
        pygame.display.flip()


menu()
