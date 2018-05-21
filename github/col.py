""" С настройками"""

import sys
import pygame

pygame.init()
n = 7  # количество клеток квадратного поля игры
width = 99  # ширина клетки( и объекта)

window = pygame.display.set_mode((693, 693))  # создаём окно
screen = pygame.Surface((693, 693))  # создаем игровое поле(экран)

pygame.display.set_caption("Dot")
pygame.font.init()

background_image=pygame.image.load('copy.jpg').convert()


BLACK = (0, 0, 0)
WHITE=(255, 255, 255)
BLUE =(0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW=(250,250,0)
PALETURQUOISE = (175, 238, 238)
GRAY = (128, 128, 128)
c=(255,255,255)

import time

pygame.mixer.music.load("04716.mp3")

#Оставаться в цикле, пока пользователь не нажмёт на кнопку закрытия окна
done=False
clock = pygame.time.Clock()


koo = []  # список нач. координат до перемещения
all_s = []  # список всех объектов
koor = []  # список координат разницы между объектом и мышкой
grid = []  # список занятых и свободных клеток
ka = []  # проверка завершенности уровня

koo2 = []  # список нач. координат до перемещения для 2 уровня
all_s2 = []  # список всех объектов для 2 уровня
koor2 = []  # список координат разницы между объектом и мышкой для 2 уровня
grid2 = []  # список занятых и свободных клеток для 2 уровня
ka2 = []  # проверка завершенности уровня для 2 уровня

done2 = False
done3 = False
dum = False
dum2 = False


for row in range(n): # заполняем пустую матрицу ka
    ka.append([])
    for column in range(n):
        ka[row].append(0)


for row in range(n): # заполняем пустую матрицу grid
    grid.append([])
    for column in range(n):
        grid[row].append(0)

for row in range(n):# заполняем пустую матрицу ka2
    ka2.append([])
    for column in range(n):
        ka2[row].append(0)

for row in range(n):# заполняем пустую матрицу grid2
    grid2.append([])
    for column in range(n):
        grid2[row].append(0)

"""Класс и объекты 1 уровня"""
class Sprite:
    # (нач.коорд-х,у,имя файла,нач.скорость-х,у)
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.image = pygame.image.load(filename)  # создаем рисунок-загрузка из файла
        self.rect = self.image.get_rect()  # представляем его прямоугольником
        all_s.append(self)
        self.w = self.h = self.image.get_width()  # ширина
        self.action = False
        self.column = self.x // (width)
        self.row = self.y // (width)
        grid[self.row][self.column] = 1
        ka[self.row][self.column] = (self.y // (width))*5 + self.x // (width)

    def bum(self):  # проверка попадания мышки на объект
        mp = pygame.mouse.get_pos()
        if self.x < mp[0] < self.x + self.w and self.y < mp[1] < self.y + self.h:
            #pygame.draw.polygon(screen, GRAY, [(self.x, self.y), (self.x + width, self.y), (self.x + width, self.y + width), (self.x, self.y + width)], 2)
            a = mp[0] - self.x  # разница кооздинаты мышки и объекта
            b = mp[1] - self.y
            koor.append(a)  # запись в список координат
            koor.append(b)
            self.action = True  # разрешение на перемещение
            c = self.x  # первоначальные координаты объекта
            d = self.y
            koo.append(c)  # запись первоначального положения выбранного объекта
            koo.append(d)

    def funtion(self):  # функция движения точно в клетку
        mp = pygame.mouse.get_pos()  # получ коорд мышки
        self.x = (mp[0] // (width)) * (width) # коорд. клетки где находится мышь
        self.y = (mp[1] // (width)) * (width)

        self.column = self.x // (width)  # координ. в списке грид
        self.row = self.y // (width)
        ka[self.row][self.column], ka[koo[1] // (width)][koo[0] // (width)] = ka[koo[1] // (width)][koo[0] // (width)], ka[self.row][self.column]
        grid[koo[1] // (width)][koo[0] // (width)] = 0  # старой клетке = 0
        if grid[self.row][self.column] == 1:  # если клетка куда переместили занята
            self.x = koo[0]  # откат на обратные координаты
            self.y = koo[1]

    def render(self):  # отображение обьекта на игровом поле(экране)
        screen.blit(self.image, (self.x, self.y))

    def mouv(self):  # движение объекта с мышкой
        pos = pygame.mouse.get_pos()  # текущее положение мышки

        # Теперь  игрок имеет координаты мышки с учетом разницы координат
        self.x = pos[0] - koor[0]
        self.y = pos[1] - koor[1]

        # условие границ поля
        if self.x < -10:
            self.x = koo[0]
            self.y = koo[1]
            self.action = False
        if self.x + width > ((width) * n + 10):
            self.x = koo[0]
            self.y = koo[1]
            self.action = False
        if self.y < -10:
            self.x = koo[0]
            self.y = koo[1]
            self.action = False
        if self.y + width > ((width) * n + 10):
            self.x = koo[0]
            self.y = koo[1]
            self.action = False


    def mesto(self):  # запись положения объектов в список грид
        self.column = self.x // (width)
        self.row = self.y // (width)
        grid[self.row][self.column] = 1

hero1 = Sprite(3*width, 4*width, ('f.1.1.jpg'))
hero2 = Sprite(4*width, 4*width, ('f.1.2.jpg'))
hero3 = Sprite(4*width, 2*width, ('f.1.3.jpg'))
hero4 = Sprite(3*width, 3*width, ('f.2.1.jpg'))
hero5 = Sprite(2*width, 3*width, ('f.2.2.jpg'))
hero6 = Sprite(2*width, 4*width, ('f.2.3.jpg'))
hero7 = Sprite(4*width, 3*width, ('f.3.1.jpg'))
hero8 = Sprite(3*width, 2*width, ('f.3.2.jpg'))
hero9 = Sprite(2*width, 2*width, ('f.3.3.jpg'))

"""Класс и объекты 2 уровня"""
class Sprite:
    # (нач.коорд-х,у,имя файла, уровень)
    def __init__(self, xpos, ypos, filename, k):
        self.x = xpos
        self.y = ypos
        self.image = pygame.image.load(filename)  # создаем рисунок-загрузка из файла
        self.rect = self.image.get_rect()  # представляем его прямоугольником
        all_s2.append(self)
        self.w = self.h = self.image.get_width()  # ширина
        self.action = False
        self.column = self.x // (width)
        self.row = self.y // (width)
        grid2[self.row][self.column] = 1
        ka2[self.row][self.column] = (self.y // (width))*5 + self.x // (width)

    def bum(self):  # проверка попадания мышки на объект
        mp = pygame.mouse.get_pos()
        if self.x < mp[0] < self.x + self.w and self.y < mp[1] < self.y + self.h:
            #pygame.draw.polygon(screen, GRAY, [(self.x, self.y), (self.x + width, self.y), (self.x + width, self.y + width), (self.x, self.y + width)], 2)
            a = mp[0] - self.x  # разница кооздинаты мышки и объекта
            b = mp[1] - self.y
            koor2.append(a)  # запись в список координат
            koor2.append(b)
            self.action = True  # разрешение на перемещение
            c = self.x  # первоначальные координаты объекта
            d = self.y
            koo2.append(c)  # запись первоначального положения выбранного объекта
            koo2.append(d)

    def funtion(self):  # функция движения точно в клетку
        mp = pygame.mouse.get_pos()  # получ коорд мышки
        self.x = (mp[0] // (width)) * (width) # коорд. клетки где находится мышь
        self.y = (mp[1] // (width)) * (width)

        self.column = self.x // (width)  # координ. в списке грид
        self.row = self.y // (width)
        ka2[self.row][self.column], ka2[koo2[1] // (width)][koo2[0] // (width)] = ka2[koo2[1] // (width)][koo2[0] // (width)], ka2[self.row][self.column]
        grid2[koo2[1] // (width)][koo2[0] // (width)] = 0  # старой клетке = 0
        if grid2[self.row][self.column] == 1:  # если клетка куда переместили занята
            self.x = koo2[0]  # откат на обратные координаты
            self.y = koo2[1]

    def render(self):  # отображение обьекта на игровом поле(экране)
        screen.blit(self.image, (self.x, self.y))

    def mouv(self):  # движение объекта с мышкой
        pos = pygame.mouse.get_pos()  # текущее положение мышки

        # Теперь  игрок имеет координаты мышки с учетом разницы координат
        self.x = pos[0] - koor2[0]
        self.y = pos[1] - koor2[1]

        # условие границ поля
        if self.x < -10:
            self.x = koo2[0]
            self.y = koo2[1]
            self.action = False
        if self.x + width > ((width) * n + 10):
            self.x = koo2[0]
            self.y = koo2[1]
            self.action = False
        if self.y < -10:
            self.x = koo2[0]
            self.y = koo2[1]
            self.action = False
        if self.y + width > ((width) * n + 10):
            self.x = koo2[0]
            self.y = koo2[1]
            self.action = False


    def mesto(self):  # запись положения объектов в список грид
        self.column = self.x // (width)
        self.row = self.y // (width)
        grid2[self.row][self.column] = 1

hero01 = Sprite(3*width, 5*width, ('1.1.jpg'), 2)
hero02 = Sprite(5*width, 1*width, ('1.2.jpg'), 2)
hero03 = Sprite(1*width, 3*width, ('1.3.jpg'), 2)
hero04 = Sprite(2*width, 1*width, ('1.4.jpg'), 2)
hero05 = Sprite(1*width, 4*width, ('1.5.jpg'), 2)
hero06 = Sprite(3*width, 4*width, ('2.1.jpg'), 2)
hero07 = Sprite(2*width, 4*width, ('2.2.jpg'), 2)
hero08 = Sprite(1*width, 2*width, ('2.3.jpg'), 2)
hero09 = Sprite(1*width, 1*width, ('2.4.jpg'), 2)
hero10 = Sprite(1*width, 5*width, ('2.5.jpg'), 2)
hero11 = Sprite(4*width, 5*width, ('3.1.jpg'), 2)
hero12 = Sprite(4*width, 4*width, ('3.2.jpg'), 2)
hero13 = Sprite(3*width, 1*width, ('3.3.jpg'), 2)
hero14 = Sprite(3*width, 3*width, ('3.4.jpg'), 2)
hero15 = Sprite(2*width, 2*width, ('3.5.jpg'), 2)
hero16 = Sprite(4*width, 1*width, ('4.1.jpg'), 2)
hero17 = Sprite(2*width, 5*width, ('4.2.jpg'), 2)
hero18 = Sprite(4*width, 2*width, ('4.3.jpg'), 2)
hero19 = Sprite(5*width, 5*width, ('4.4.jpg'), 2)
hero20 = Sprite(2*width, 3*width, ('4.5.jpg'), 2)
hero21 = Sprite(5*width, 3*width, ('5.1.jpg'), 2)
hero22 = Sprite(5*width, 4*width, ('5.2.jpg'), 2)
hero23 = Sprite(3*width, 2*width, ('5.3.jpg'), 2)
hero24 = Sprite(4*width, 3*width, ('5.4.jpg'), 2)
hero25 = Sprite(5*width, 2*width, ('5.5.jpg'), 2)


""" Меню, выбор действия"""
class Menu:
    def __init__(self, punkts):
        self.punkts = punkts
    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0],i[1]))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self):
        done = True
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0,0)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            screen.blit(background_image, [0, 0])
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+55:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()

            window.blit(screen, (0, 0))
            # Обновить экран, выведя то, что мы нарисовали
            pygame.display.flip()


punkts = [(250, 250, u'Начать игру', (250, 250, 30), (250, 30, 250), 0),
          (290, 320 , u'Выход', (250, 250, 30), (250, 30, 250),1)]
game = Menu(punkts)
game.menu()

# выбор уровня
done1 = True
while done1:
    window.blit(background_image, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.draw.rect(window, BLACK, [198, 198, 297, 132])
    pygame.draw.rect(window, BLACK, [198, 363, 297, 132])
    pygame.draw.rect(window, WHITE, [203, 203, 287, 122])
    pygame.draw.rect(window, WHITE, [203, 368, 287, 122])

    font = pygame.font.Font(None, 50)
    text = font.render("1 уровень", True, BLACK)
    window.blit(text, [238, 248])

    font = pygame.font.Font(None, 50)
    text = font.render("2 уровень", True, BLACK)
    window.blit(text, [238, 416])

    # отмечается другим цветом при наведении
    pos = pygame.mouse.get_pos()
    x1 = pos[0]
    y1 = pos[1]
    if x1 < 490 and x1 > 203:
        if y1 > 203 and y1 < 325:
            pygame.draw.rect(window, PALETURQUOISE, [203, 203, 287, 122])
            font = pygame.font.Font(None, 50)
            text = font.render("1 уровень", True, BLACK)
            window.blit(text, [238, 248])
        if y1 > 368 and y1 < 490:
            pygame.draw.rect(window, PALETURQUOISE, [203, 368, 287, 122])
            font = pygame.font.Font(None, 50)
            text = font.render("2 уровень", True, BLACK)
            window.blit(text, [238, 416])
    # нажатие
    if pygame.mouse.get_pressed()[0]:
        if x1 < 490 and x1 > 203:
            if y1 > 203 and y1 < 325:
                dum = True
                done2 = True
                done1 = False
            if y1 > 368 and y1 < 490:
                dum2 = True
                done3 = True
                done1 = False


    # Обновить экран, выведя то, что мы нарисовали
    pygame.display.flip()

while dum:  # условие существования игрового цикла

    screen.fill((220, 220, 220))

    for e in pygame.event.get():  # для любого события
        if e.type == pygame.QUIT:  # если было закрытие окна
            sys.exit()

    # захват объекта лкм и перемещение при удержании кнопки
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            for i in all_s:  # захват объекта
                i.bum()

        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:  # если отпущена лкм
            for i in all_s:
                if i.action == True:
                    i.funtion()  # перемещение объекта точно в клетку
            for i in all_s:
                i.action = False  # движение запрещено

            for i in all_s:  # запись положения объекта в список grid
                i.mesto()
            koor = []  # список координат разницы между объектом и мышкой
            koo = []  # обнуление списка захвачен. объекта

    for i in all_s:
        if i.action == True:
            i.mouv()  # перемещение объекта мышкой
        i.render()  # отображаем все объекты
    if ka == [[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0], [0, 0, 23, 24, 14, 0, 0], [0, 0, 18, 17, 22, 0, 0],
              [0, 0, 19, 13, 12, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]: # пазл собран
        while done2:
            for e in pygame.event.get():  # для любого события
                if e.type == pygame.QUIT:  # если было закрытие окна
                    sys.exit()

            pygame.draw.rect(screen, BLACK, [198, 248, 296, 197])
            pygame.draw.rect(screen, WHITE, [203, 253, 286, 187])

            font = pygame.font.Font(None, 50)
            text = font.render("YOU WIN!", True, BLACK)
            screen.blit(text, [268, 327])

            pygame.draw.rect(screen, BLACK, [424, 405, 70, 40])
            pygame.draw.rect(screen, WHITE, [429, 410, 60, 30])

            font = pygame.font.Font(None, 25)
            text = font.render("Ok", True, BLACK)
            screen.blit(text, [447, 418])

            pygame.draw.rect(screen, BLACK, [198, 405, 70, 40])
            pygame.draw.rect(screen, WHITE, [203, 410, 60, 30])

            font = pygame.font.Font(None, 25)
            text = font.render("Menu", True, BLACK)
            screen.blit(text, [213, 418])

            if pygame.mouse.get_pressed()[0]:
                mp = pygame.mouse.get_pos()
                if mp[1] < 440 and mp[1] > 410:
                    if mp[0] < 489 and mp[0] > 429: # выбран Ок
                        dum2 = True
                        done3 = True
                        done2 = False
                    if mp[0] < 263 and mp[0] > 203: # выбрано меню
                        done = True
                        done2 = False
            window.blit(screen, (0, 0))  # на окне прорисовываем поле игры
            pygame.display.flip()  # отображаем полностью дисплей(окно)
    if done: #возврат к меню
        screen.fill((220, 220, 220))
        game.menu()
    if dum2: #переход на 2 уровень
        dum = False


    window.blit(screen, (0, 0))  # на окне прорисовываем поле игры
    pygame.display.flip()  # отображаем полностью дисплей(окно)


while dum2:  # условие существования игрового цикла

    screen.fill((220, 220, 220))

    for e in pygame.event.get():  # для любого события
        if e.type == pygame.QUIT:  # если было закрытие окна
            sys.exit()

            # захват объекта лкм и перемещение при удержании кнопки
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            for i in all_s2:  # захват объекта
                i.bum()

        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:  # если отпущена лкм
            for i in all_s2:
                if i.action == True:
                    i.funtion()  # перемещение объекта точно в клетку
            for i in all_s2:
                i.action = False  # движение запрещено

            for i in all_s2:  # запись положения объекта в список grid
                i.mesto()  # запись положения объектов в список грид
            koor2 = []  # список координат разницы между обьуктом и мышкой
            koo2 = []  # обнуление списка захвачен. объекта

    for i in all_s2:
        if i.action == True:
            i.mouv()  # перемещение объекта мышкой
        i.render()  # отображаем все объекты

    if ka2 == [[0, 0, 0, 0, 0, 0, 0], [0, 28, 10, 16, 7, 21, 0], [0, 23, 22, 11, 6, 26, 0], [0, 29, 24, 8, 18, 12, 0],
               [0, 9, 27, 14, 30, 17, 0], [0, 20, 25, 13, 19, 15, 0], [0, 0, 0, 0, 0, 0, 0]]: # пазл собран
        while done3:
            for e in pygame.event.get():  # для любого события
                if e.type == pygame.QUIT:  # если было закрытие окна
                    sys.exit()

            pygame.draw.rect(screen, BLACK, [198, 248, 296, 197])
            pygame.draw.rect(screen, WHITE, [203, 253, 286, 187])

            font = pygame.font.Font(None, 50)  # мои поздравления
            text = font.render("YOU WIN!", True, BLACK)
            screen.blit(text, [268, 327])

            pygame.draw.rect(screen, BLACK, [424, 405, 70, 40])
            pygame.draw.rect(screen, WHITE, [429, 410, 60, 30])

            font = pygame.font.Font(None, 25)
            text = font.render("Ok", True, BLACK)
            screen.blit(text, [447, 418])

            pygame.draw.rect(screen, BLACK, [198, 405, 70, 40])
            pygame.draw.rect(screen, WHITE, [203, 410, 60, 30])

            font = pygame.font.Font(None, 25)
            text = font.render("Menu", True, BLACK)
            screen.blit(text, [213, 418])

            if pygame.mouse.get_pressed()[0]:
                mp = pygame.mouse.get_pos()
                if mp[1] < 440 and mp[1] > 410:
                    if mp[0] < 489 and mp[0] > 429: # выбран Ок
                        done = True
                        done3 = False
                    if mp[0] < 263 and mp[0] > 203: # выбрано меню
                        done = True
                        done3 = False
            window.blit(screen, (0, 0))  # на окне прорисовываем поле игры
            pygame.display.flip()  # отображаем полностью дисплей(окно)
    if done: # возврат к меню
        screen.fill((220, 220, 220))
        game.menu()
    window.blit(screen, (0, 0))  # на окне прорисовываем поле игры
    pygame.display.flip()  # отображаем полностью дисплей(окно)

pygame.quit ()