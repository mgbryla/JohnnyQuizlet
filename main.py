import random as rd

MENU = 'JohnnyQuizlet\n\nWybierz opcję wpisując numer.\n1.Startuj!\n2.Zamknij.' \
       '\n\nNIE WCISKAJ NIC INNEGO, BO PROGRAM UMRZE'
INNE = 'Wybierz z podanych opcji'
MENU2 = '1.Dodaj listę.\n2.Pokaż listę.\n3.Usuń listę.\n4.Losuj.\n 5. Wróć'


def pierwsza_strona():
    start = '0'
    while True:
        if start == '0':
            print(MENU)
            start = input()
        elif start == '1':
            print(MENU2)
            while True:
                wybor = input()
                if wybor == '1':
                    słówka = input('Wpisz słowa oddzielone spacją: ')
                    lista = słówka.split()
                    break
                elif wybor == '2':
                    try:
                        print(lista)
                    except UnboundLocalError:
                        print('Brak listy.')
                    break
                elif wybor == '3':
                    try:
                        del lista
                        print('Usunięto listę.')
                    except UnboundLocalError:
                        print('Brak listy.')
                    break
                elif wybor == '4':
                    try:
                        print("\033[1m" + rd.choice(lista) + "\033[1m")
                        print('\033[0m')
                    except UnboundLocalError:
                        print('Brak listy.')
                    break
                elif wybor == '5':
                    start = '0'
                    break
                else:
                    print(INNE)
                break
        elif start != '2':                      # poprzednio ta i następna opcja były zamienione
            print(INNE)                         # ale przy inpucie innym niż 1 lub 2 printowało INNE w nieskończoność
            break                               # a break psuł zmienne 'lista' i 'słówka'
        else:                                   # teraz nie pisze w nieskończoność, za to kończy program
            print('Do widzenia, do jutra!')     # nie mam pewności czy to postęp czy regres
            break                               # z pozdrowieniami, typ niepokorny


pierwsza_strona()
