import random


def wypelniona_tablica():
    tablica_liczb = []
    for i in range(50):
        tablica_liczb.append(random.randrange(1,100))
    return tablica_liczb


def szukanie_z_wartownikiem(tablica_z_szukana, n):
    x = int(input("Podaj szukaną: "))
    wartownik = tablica_z_szukana.append(x)
    for i in range(n):
        if tablica_z_szukana[i] == x and i != n+1:
            for j in range(n-1):
                print(tablica_z_szukana[j], end=", ")
            print("\nWartość znaleziona pod indeksem: ", i)
            return

    for i in range(n - 1):
        print(tablica_z_szukana[i], end=", ")
    print("\nNie znaleziono elementu w tej tablicy")


szukanie_z_wartownikiem(wypelniona_tablica(), 50)