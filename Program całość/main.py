# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

import linecache
import random



lista_zapisanych_graczy = {}
aktualny_gracz = 0

# ********************WYBÓR HASŁA WEDŁUG TRUDNOŚCI I KATEGORI**********************:

def choose_a_word_easy(kategoria_hasla: str) -> str:
    with open("Hasla_latwe") as hasla:
        nr_wiersza = 0
        for wiersz in hasla:
            linia = wiersz
            nr_wiersza += 1
            if kategoria_hasla in linia:
                wiersz_hasel = linecache.getline("Hasla_latwe", nr_wiersza + 1)

    wiersz_hasel = wiersz_hasel.split(" ")
    liczba_slow = len(wiersz_hasel)
    losowa_liczba = random.randint(0, liczba_slow - 1)
    haslo_result = wiersz_hasel[losowa_liczba]

    return haslo_result

def choose_a_word_medium(kategoria_hasla: str) -> str:
    with open("Hasla_srednie") as hasla:
        nr_wiersza = 0
        for wiersz in hasla:
            linia = wiersz
            nr_wiersza += 1
            if kategoria_hasla in linia:
                wiersz_hasel = linecache.getline("Hasla_srednie", nr_wiersza + 1)

    wiersz_hasel = wiersz_hasel.split(" ")
    liczba_slow = len(wiersz_hasel)
    losowa_liczba = random.randint(0, liczba_slow - 1)
    haslo_result = wiersz_hasel[losowa_liczba]

    return haslo_result


def choose_a_word_high(kategoria_hasla: str) -> str:
    with open("Hasla_trudne") as hasla:
        nr_wiersza = 0
        for wiersz in hasla:
            linia = wiersz
            nr_wiersza += 1
            if kategoria_hasla in linia:
                wiersz_hasel = linecache.getline("Hasla_trudne", nr_wiersza + 1)

    wiersz_hasel = wiersz_hasel.split(" ")
    liczba_slow = len(wiersz_hasel)
    losowa_liczba = random.randint(0, liczba_slow - 1)
    haslo_result = wiersz_hasel[losowa_liczba]

    return haslo_result
# ***************************************************************************************



# ***************************OBSŁUGA WYBORU HASŁA**********************************************

def choose_password(poziom, kategoria) -> str:
    if poziom == 1:
        password = choose_a_word_easy(kategoria)
    elif poziom == 2:
        password = choose_a_word_high(kategoria)
    else:
        password = choose_a_word_high(kategoria)
    return password
#************************************************************************************************



# ***************************WYBÓR KATEGORI**********************************************

def choose_category(dostepne_kategorie: dict):
    kategoria = int(input("Wybierz Kategorie:\n"
                          "Wpisz liczbę od 1-5 a następmnie wciśnij enter\n"
                          "1 - Zwierzęta\n"
                          "2 - Rzeczy\n"
                          "3 - Owoce i Warzywa\n"
                          "4 - Państwa\n"
                          "5 - Losowo\n"
                          "Wpisz i zaakceptuj:"))
    if kategoria == 5:
        losowy = random.randint(1, 4)
        print("Wybraliśmy za ciebie kategorie: ", dostepne_kategorie[losowy])
        kategoria = losowy
    else:
        print("Wybrałeś kategorie: ", dostepne_kategorie[kategoria])

    return kategoria
#************************************************************************************************



# ***************************WYBÓR POZIOMU TRUDNOŚCI**********************************************

def choose_level(dostepne_poziomy: dict):
    trudnosc = int(input("Wybierz Poziom Trudności:\n"
                          "Wpisz 1,2 lub 3 a następmnie wciśnij enter\n"
                          "1 - Łatwy\n"
                          "2 - Średni\n"
                          "3 - Trudny\n"
                          "4 - Losowo\n"
                          "Wpisz i zaakceptuj:"))
    if trudnosc == 4:
        losowy = random.randint(1,3)
        print("Wybraliśmy za ciebie: ", dostepne_poziomy[losowy])
        trudnosc = losowy
    else:
        print("Wybrałeś: ", dostepne_poziomy[trudnosc] )

    return  trudnosc
#************************************************************************************************

# ***************************POCZĄTEK GRY**********************************************
def start() ->int:
    global aktualny_gracz
    global lista_zapisanych_graczy
    dostepne_poziomy = {1: "Łatwy poziom trudności", 2: "Średni poziom trudnośći", 3: "Wysoki poziom trudności"}
    dostepne_kategorie = {1: "Zwierzeta", 2: "Rzeczy", 3: "Owoce i Warzywa", 4: "Panstwa"}

    begin_game()
    poczatkowy_wybor = int(input("Wybierz:\n"
                             "1 : Rospoccznik grę\n"
                             "2 : Zobacz Ranking\n"
                             "3 : Wyjdź\n"
                             "W pisz i zatwierdź enterem: "))
    print("\n")
    if poczatkowy_wybor == 2:
        ranking_game()
        start()
    elif poczatkowy_wybor == 3:
        return 0
    print("\n")
    tworzenie = ask_creat_account()
    if tworzenie == 0:
        aktualny_gracz = choose_own_profil()
        print("Witaj! ",lista_zapisanych_graczy[str(aktualny_gracz)][0] + " " + lista_zapisanych_graczy[str(aktualny_gracz)][1])
        if aktualny_gracz == 0:
            nick = input("Aby stworzyć gracza wpisz imie i nazwisko:")
            nick = nick.split(" ")
            creat_account(nick[0], nick[1])

    ask_next_game = 1
    while ask_next_game == 1:
        poziom = choose_level(dostepne_poziomy)
        print("\n\n")
        kategoria = choose_category(dostepne_kategorie)
        password = choose_password(poziom, dostepne_kategorie[kategoria])
        print("\n\n")
        guess_password(password)
        ask_next_game = end_game()
    return start()
#************************************************************************************************


#***************************ZGADYWANIE HASŁA*****************************************************
def guess_password(password) -> int:
    l_zyc = 6
    dlugosc_slowa_na_poczatku = len(password)
    password = password.lower()
    wynik = []
    slowo = {}
    zgadywane = []
    # print(password)
    d_slowa = len(password)

    for i in range(0, d_slowa):
        slowo[i] = password[i]
        wynik.extend("_")
    # print(slowo)
    for char in wynik:
        print(char, " ", end="")
    print("\npowodzenia w zgadywaniu: ")
    while l_zyc > 0 and d_slowa > 0:
        traf = 0
        ilosc_trafionych_liter = 0
        wpisany_znak = input("\nwpisz wybraną literę a następnie zatwierdź:")
        if wpisany_znak in zgadywane:
            print("już podałeś tą litere :(")
            continue
        else:
            zgadywane.extend(wpisany_znak)

        for key, value in slowo.items():
            if value == wpisany_znak:
                wynik[key] = value
                traf = 1
                ilosc_trafionych_liter += 1
        if traf == 1:
            print("trafiony!")
            d_slowa = d_slowa -ilosc_trafionych_liter
        else:
            print("pudło!")
            l_zyc = l_zyc - 1
        for char in wynik:
            print(char, " ", end="")

    if l_zyc > 0:
        print("\nBrawo udało ci się, Świetna robota!!")
    else:
        print("\nNastępnym razem na pewno pójdzie ci lepiej!!")

    print("twoja liczba punktów to:")
    uzyskany_wynik = make_result(l_zyc, d_slowa, dlugosc_slowa_na_poczatku)
    print(uzyskany_wynik)
    save_result(uzyskany_wynik)

    return uzyskany_wynik


#***************************OBLICZANIE WYNIKU*****************************************************
def make_result(l_zyc, d_slowa, dlugosc_slowa_na_poczatku) -> int:
    if d_slowa == 0:
        uzyskany_wynik = (l_zyc*50 + (dlugosc_slowa_na_poczatku - d_slowa) *20) + 200
    else:
        uzyskany_wynik = l_zyc * 50 + (dlugosc_slowa_na_poczatku - d_slowa) * 20 + 40
    return uzyskany_wynik
#************************************************************************************************


#***************************SZYBKIE TESTY*****************************************************
def to_test(x, y) -> None:
    global aktualny_gracz
    global  lista_zapisanych_graczy
    aktualny_gracz = x
    lista_zapisanych_graczy = y


#************************************************************************************************


#***************************ZNAJDOWANIE GRACZA*****************************************************
def choose_own_profil() -> int:
    save_dict = {}
    with open("Zapis i Odczyt") as file:
        for line in file:
            if ":" in line:
                save = line.split(" ")
                save_dict[int(save[0][0])] = save[1] + " " + save[2]

    for key, value in save_dict.items():
        print(key,":", value)

    wybor = input("Wpisz liczbę całkowitą występującą obok twojego niku,\nJeśli się nie znalazłeś wpisz 0: ")
    return int(wybor)
#************************************************************************************************


#***************************TWORZENIE GRACZA*****************************************************
def ask_creat_account() -> int:
    resul = input("Masz konto?\nWpisz tak lub nie:")
    result = 1 if "nie" in resul else 0
    if result == 1:
        nick = input("Aby stworzyć gracza wpisz imie i nazwisko:")
        nick = nick.split(" ")
        creat_account(nick[0], nick[1])
        return 1
    else:
        return 0


def creat_account(name: str, surname: str) -> None:
    global aktualny_gracz
    liczba_graczy = len(lista_zapisanych_graczy)
    lista_zapisanych_graczy[str(liczba_graczy+1)] = [name, surname, 0]
    aktualny_gracz = liczba_graczy + 1
    print("Witaj! ", lista_zapisanych_graczy[str(aktualny_gracz)][0] +" "+ lista_zapisanych_graczy[str(aktualny_gracz)][1])


#***************************WCZYTANIE ZAPISANYCH WYNIKÓW*****************************************************
def begin_game() -> None:
    with open("Zapis i Odczyt") as file:
        wynik = 0
        for line in file:
            lin = line.split(" ")
            wynik = int(lin[3])
            lista_zapisanych_graczy[lin[0][0]] = [lin[1],lin[2], wynik]
#************************************************************************************************


#***************************ZAPISANIE WYNIKU*****************************************************
def save_result(result_with_game) -> None:
    lista_zapisanych_graczy[str(aktualny_gracz)][2] += result_with_game
#************************************************************************************************


#***************************ZAPISANIE GRY*****************************************************
def save_game() -> None:
    with open("Zapis i Odczyt", 'w') as file:
        for key, value in lista_zapisanych_graczy.items():
            chars = '{key}: {value[0]} {value[1]} {value[2]}\n'.format(key=key, value=value)
            file.write(chars)

#************************************************************************************************


#***************************ZAKOŃCZENIE GRY*****************************************************
def end_game() -> int:
    resul = input("Che chcesz zagrać jeszce raz ? Wpisz tak lub nie: ")
    result = 1 if "nie" in resul else 0
    if result == 1:
        save_game()
        return 0
    else:
        return 1
#************************************************************************************************

#***************************RANKING GRY*****************************************************
def ranking_game() -> None:
    lista_zapisanych_graczy_pomocnicza = lista_zapisanych_graczy
    miejsce = 1
    max_key = ""
    print("RANKING GRY!!!")
    while lista_zapisanych_graczy_pomocnicza != {}:
        aktualny_wartosc = 0
        for key in lista_zapisanych_graczy_pomocnicza.keys():
            if lista_zapisanych_graczy_pomocnicza[key][2] > aktualny_wartosc:
                aktualny_wartosc = lista_zapisanych_graczy_pomocnicza[key][2]
                max_key = key
        print(miejsce,". ",'{0:30s} {1:<2.0f}'.format(lista_zapisanych_graczy[str(max_key)][0] +" "+ lista_zapisanych_graczy[str(max_key)][1], aktualny_wartosc))

        miejsce += 1
        del lista_zapisanych_graczy_pomocnicza[str(max_key)]
    print("\n")
    input("Aby wyjść wciśnij dowolny klawisz a następnie enter")



#************************************************************************************************



# class Account:
#     id_number = 0
#
#     def __init__(self,  name: str, surname: str, result=0):
#         self.id =  self.generate_id()
#         self.name = name
#         self.surname = surname
#         self.result = result
#
#     def __str__(self):
#         return '{self.id}: {self.name} {self.surname}\nresult = {self.result}'.format(self = self)
#
#     def get_result(self):
#         return self.result
#
#     @classmethod
#     def generate_id(cls):
#         cls.id_number += 1
#         return cls.id_number


#************************************************************************************************






if __name__ == '__main__':
    start()
    #fast_test()
