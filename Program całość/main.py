# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

import linecache
import random



# ********************WYBÓR HASŁA WEDŁUG TRUDNOŚCI I KATEGORI**********************:

def choose_a_word_easy(kategoria_hasla: str) -> str:
    with open("Hasla_latwe") as hasla:
        nr_wiersza = 0
        for wiersz in hasla:
            linia = wiersz
            nr_wiersza += 1
            if kategoria_hasla in linia:
                wiersz_hasel = linecache.getline("Hasla_latwe", nr_wiersza + 1)

    liczba_slow = 0
    for char in wiersz_hasel:
        if char == " ":
            liczba_slow += 1

    losowa_liczba = random.randint(0, liczba_slow - 1)

    liczba_slow = 0
    haslo_result = ""
    for char in wiersz_hasel:
        if char == " ":
            liczba_slow += 1
            continue
        if liczba_slow == losowa_liczba:
            haslo_result = haslo_result + char

    return haslo_result

def choose_a_word_medium(kategoria_hasla: str) -> str:
    with open("Hasla_srednie") as hasla:
        nr_wiersza = 0
        for wiersz in hasla:
            linia = wiersz
            nr_wiersza += 1
            if kategoria_hasla in linia:
                wiersz_hasel = linecache.getline("Hasla_srednie", nr_wiersza + 1)

    liczba_slow = 0
    for char in wiersz_hasel:
        if char == " ":
            liczba_slow += 1

    losowa_liczba = random.randint(0, liczba_slow -1)

    liczba_slow = 0
    haslo_result = ""
    for char in wiersz_hasel:
        if char == " ":
            liczba_slow += 1
            continue
        if liczba_slow == losowa_liczba:
            haslo_result = haslo_result + char

    return haslo_result

def choose_a_word_high(kategoria_hasla: str) -> str:
    with open("Hasla_trudne") as hasla:
        nr_wiersza = 0
        for wiersz in hasla:
            linia = wiersz
            nr_wiersza += 1
            if kategoria_hasla in linia:
                wiersz_hasel = linecache.getline("Hasla_trudne", nr_wiersza + 1)

    liczba_slow = 0
    for char in wiersz_hasel:
        if char == " ":
            liczba_slow += 1

    losowa_liczba = random.randint(0, liczba_slow - 1)

    liczba_slow = 0
    haslo_result = ""
    for char in wiersz_hasel:
        if char == " ":
            liczba_slow += 1
            continue
        if liczba_slow == losowa_liczba:
            haslo_result = haslo_result + char

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
def start() ->None:
    dostepne_poziomy = {1: "Łatwy poziom trudności", 2: "Średni poziom trudnośći", 3: "Wysoki poziom trudności"}
    dostepne_kategorie = {1: "Zwierzeta", 2: "Rzeczy", 3: "Owoce i Warzywa", 4: "Panstwa"}
    poziom = choose_level(dostepne_poziomy)
    print("\n\n")
    kategoria = choose_category(dostepne_kategorie)
    password = choose_password(poziom, dostepne_kategorie[kategoria])
    print("\n\n")
    guess_password(password)
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

    return uzyskany_wynik


#***************************OBLICZANIE WYNIKU*****************************************************
def make_result(l_zyc, d_slowa, dlugosc_slowa_na_poczatku) -> int:
    if d_slowa == 0:
        uzyskany_wynik = (l_zyc*50 + (dlugosc_slowa_na_poczatku - d_slowa) *20) + 200
    else:
        uzyskany_wynik = l_zyc * 50 + (dlugosc_slowa_na_poczatku - d_slowa) * 20 + 40
    return uzyskany_wynik
#************************************************************************************************






if __name__ == '__main__':
    start()
