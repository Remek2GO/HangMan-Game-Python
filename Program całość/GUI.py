#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame, sys
from copy import deepcopy

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wisielec")
FPS_menu = 30



class Object:
    def __init__(self, x_cord, y_cord, file_name):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.button_immage = pygame.image.load(f"{file_name[:-4]}.png")

    def draw_object(self, window):
        window.blit(self.button_immage, (self.x_cord, self.y_cord))

class Button:
    def __init__(self, x_cord, y_cord, file_name):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.button_immage = pygame.image.load(f"{file_name[:-4]}.png")
        self.hovered_button_immage = pygame.image.load(f"{file_name[:-4]}_hovered.png")
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.button_immage.get_width(), self.button_immage.get_height())

    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
    def draw(self, window):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.hovered_button_immage, (self.x_cord, self.y_cord))
        else:
            window.blit(self.button_immage, (self.x_cord, self.y_cord))


class ButtonWrite:
    def __init__(self, x_cord, y_cord, name):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.button_write = name
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, 200, 35)

    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

class Blank:
    def __init__(self, file_name_menu):
        self.x = 0
        self.y = 0
        self.file_name_menu = pygame.image.load(f"{file_name_menu[:-4]}.png")

    def draw_menu(self, window):
        window.blit(self.file_name_menu, (self.x, self.y))




def start_gui() -> int:
    pygame.time.delay(100)
    pygame.display.update()
    tlo_1 = Blank('zdjecia_interfejs/menu.png')
    rozpocznij_gre_button = Button(275, 250, "zdjecia_interfejs/rozpocznij_gre.png")
    zobacz_ranking_buton = Button(275, 250 + 75, "zdjecia_interfejs/zobacz_ranking.png")
    wyjdz_buton = Button(275, 250 + 75+75, "zdjecia_interfejs/wyjdz.png")

    while True:
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        tlo_1.draw_menu(window)
        rozpocznij_gre_button.draw(window)
        zobacz_ranking_buton.draw(window)
        wyjdz_buton.draw(window)
        if rozpocznij_gre_button.tick() == 1:
            return 1
        elif zobacz_ranking_buton.tick() == 1:
            return 2
        elif wyjdz_buton.tick() == 1:
            return 3

        pygame.display.update()


def account():
    pygame.time.delay(100)
    pygame.display.update()
    tlo_2 = Blank('zdjecia_interfejs/masz_konto.png')
    tak_button = Button(275, 250, "zdjecia_interfejs/tak.png")
    nie_buton = Button(275, 250 + 75, "zdjecia_interfejs/nie.png")
    while True:
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        tlo_2.draw_menu(window)
        tak_button.draw(window)
        nie_buton.draw(window)
        if tak_button.tick():
            return 2
        elif nie_buton.tick():
            return 1


        pygame.display.update()


def ranking(lista_zapisanych_graczy) -> int:
    pygame.time.delay(100)
    pygame.display.update()
    tlo = Blank('zdjecia_interfejs/tlo.png')
    tlo_ranking = Object(275,50,'zdjecia_interfejs/ranking.png')
    wyjdz_ranking_button = Button(520, 520, "zdjecia_interfejs/wyjdz.png")
    font = pygame.font.SysFont("Comic Sans MS", 18)

    while True:
        miejsce = 1
        max_key = ""
        y_pos = 125
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        tlo.draw_menu(window)
        tlo_ranking.draw_object(window)
        wyjdz_ranking_button.draw(window)

        lista_zapisanych_graczy_pomocnicza = deepcopy(lista_zapisanych_graczy)

        while lista_zapisanych_graczy_pomocnicza != {}:
            aktualny_wartosc = 0
            for key in lista_zapisanych_graczy_pomocnicza.keys():
                if lista_zapisanych_graczy_pomocnicza[key][2] > aktualny_wartosc:
                    aktualny_wartosc = lista_zapisanych_graczy_pomocnicza[key][2]
                    max_key = key
            text = font.render('{0:4d}. {1:30s}'.format(miejsce, lista_zapisanych_graczy[str(max_key)][0] +" "+ lista_zapisanych_graczy[str(max_key)][1]), False, [128, 64, 255])
            wynik = font.render('{0:}'.format(aktualny_wartosc), False, [128, 64, 255])
            miejsce += 1
            window.blit(text, [250, y_pos])
            window.blit(wynik, [500, y_pos])
            del lista_zapisanych_graczy_pomocnicza[str(max_key)]
            y_pos += 20

        wyjdz_ranking_button.draw(window)

        if wyjdz_ranking_button.tick():
            return 1
        pygame.display.update()



def creat_account_gui() -> list:
    pygame.time.delay(100)
    pygame.display.update()
    tlo_tworzenie_konta = Blank('zdjecia_interfejs/tworzenie_konta.png')
    dalej_button = Button(520, 520, "zdjecia_interfejs/dalej.png")
    base_font = pygame.font.Font(None, 50)
    font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(220,320,140,50)
    color = pygame.Color('grey')
    tlo_tworzenie_konta.draw_menu(window)
    dalej_button.draw(window)
    pygame.display.flip()



    while True:
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    return user_text

        tlo_tworzenie_konta.draw_menu(window)
        pygame.draw.rect(window, color, input_rect, 2)
        text = base_font.render(user_text, True, [0, 0, 0])
        window.blit(text, (input_rect.x+5, input_rect.y +10))
        input_rect.w = max(350,text.get_width()+10)
        window.blit(font.render("Imię i Nazwisko: ", True, [0, 0, 0]) ,(input_rect.x - 190, input_rect.y +15))
        dalej_button.draw(window)
        pygame.display.flip()

        if dalej_button.tick():
            return user_text


def choose_own_profil_gui() -> int:
    pygame.time.delay(100)
    tlo = Blank('zdjecia_interfejs/tlo.png')
    tlo_wybierz = Object(275,50,'zdjecia_interfejs/wybierz.png')
    tlo.draw_menu(window)
    tlo_wybierz.draw_object(window)


    font = pygame.font.Font(None, 30)

    while True:
        button = {}
        save_dict = {}
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        with open("Zapis i Odczyt") as file:
            for line in file:
                if ":" in line:
                    save = line.split(" ")
                    save_dict[int(save[0][0])] = save[1] + " " + save[2]
        d = 200
        for key, value in save_dict.items():
            text = font.render( '{key}: {value}'.format(key= key, value = value), True, [0, 0, 0])
            window.blit(text, [300,  d])
            button[key] = ButtonWrite(300,  d, value)
            d += 30
        pygame.display.update()

        for key in button.keys():
            if button[key].tick():
                pygame.display.update()

                return key

        tlo.draw_menu(window)
        tlo_wybierz.draw_object(window)



def choose_level_gui() -> int:
    pygame.time.delay(100)
    tlo = Blank('zdjecia_interfejs/poziom_trudnosci.png')
    x = 200
    latwy_button = Button(275, x, "zdjecia_interfejs/przycisk_latwy.png")
    sredni_buton = Button(275, x + 75, "zdjecia_interfejs/przycisk_sredni.png")
    trudny_buton = Button(275, x + 75 + 75, "zdjecia_interfejs/przycisk_trudny.png")
    losowy_buton = Button(275, x + 75 + 75 + 75, "zdjecia_interfejs/przycisk_losowo.png")
    tlo.draw_menu(window)
    pygame.display.update()


    while True:
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        tlo.draw_menu(window)
        latwy_button.draw(window)
        sredni_buton.draw(window)
        trudny_buton.draw(window)
        losowy_buton.draw(window)
        pygame.display.update()
        if latwy_button.tick():
            return 1
        elif sredni_buton.tick():
            return 2
        elif trudny_buton.tick():
            return 3
        elif losowy_buton.tick():
            return 4

        pygame.display.update()

def choose_category_gui() -> int:
    pygame.time.delay(100)
    tlo = Blank('zdjecia_interfejs/kategoria.png')
    x = 150
    zwierzeta_button = Button(275, x, "zdjecia_interfejs/przycisk_zwierzeta.png")
    rzeczy_buton = Button(275, x + 75, "zdjecia_interfejs/przycisk_rzeczy.png")
    owoce_buton = Button(275, x + 75 + 75, "zdjecia_interfejs/przycisk_owoce.png")
    panstwa_buton = Button(275, x + 75 + 75 + 75, "zdjecia_interfejs/przycisk_panstwa.png")
    losowy_buton = Button(275, x + 75 + 75 + 75 + 75, "zdjecia_interfejs/przycisk_losowo.png")
    tlo.draw_menu(window)
    pygame.display.update()


    while True:
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        tlo.draw_menu(window)
        zwierzeta_button.draw(window)
        rzeczy_buton.draw(window)
        owoce_buton.draw(window)
        panstwa_buton.draw(window)
        losowy_buton.draw(window)

        if zwierzeta_button.tick():
            return 1
        elif rzeczy_buton.tick():
            return 2
        elif owoce_buton.tick():
            return 3
        elif panstwa_buton.tick():
            return 4
        elif panstwa_buton.tick():
            return 5
        pygame.display.update()


















