'''
To jest moduł wyjściowy który powinien zostać uruchomiony w celu sprawnego działania całego generatora kolokwiów. 
Pozwala użytkownikowi wybrać z menu dwie opcje:

1) Tworzenie pojedyńczego kolokwia bazującego na imieniu oraz nazwisku podanego przez użytkownika
2) Tworzenie więcej niż jednego kolokwia bazując na wybranym pliku typu excel zdefiniowanym jako "imiona.ods"

Każda z opcji pozwala użytkownikowi wybrać do 5 zadań których poszczególne elementy zmieniają się bazując na "liczbie studenta" w celu utrudnienia ściąganiu.
Korzysta z funkcji ze wszystkich trzech modułów.
Oddaje folder "biblioteka_liczb_stud" zawierający pliki tekstowe z informacją o poszczególnym studencie i jego liczbie.
Wszystkie te informacje są skompresowane w jednym pliku "liczby_studentow.txt", gdzie można przejrzeć imiona i nazwiska studentów oraz odpowiadające im liczby.
Oddaje również folder z kolokwiami w formacie .ipynb. Każde z nich jest przypisane do każdego studenta, na co wskazuje nazwa w pliku bądź jego samego.
'''

import liczba_studenta, kolokwia_generator ,importowanie_excel 


def menu(): 
    '''
    Główna funkcja zrzeszająca wszystkie funkcje w celu wywołania poprawnie całego programu i wygenerowania kolokwium/ów
    
    Funkcaj posiada wybór między wygenerowaniem jednego kolowium a impotem pliku excel i wygenerowania odpowiadającej jej liczbie.
    '''

    while True:
        wybor = input('Wybierz jedną z opcji poniżej: \n1 - Generator pojedyńczego kolokwia \n2 - Generator kolokwiów z pliku excel\n')
       
        try:
            wybor = int(wybor)
        except Exception:
            print('Niepoprawna wartość. Proszę wybrać numer opcji\n')
            continue

        
        if wybor == 1:
            
            liczba_studenta.wprowadz_imie_nazwisko_stu()
            liczba_studenta.zmien_litery_ins()
            liczba_studenta.finalna(liczba_studenta.im_nazw_studenta)
            liczba_studenta.zapis_sprawdz(liczba_studenta.im_nazw_studenta_lower, liczba_studenta.finalna_liczba)
            liczba_studenta.liczby_studentow_wszystkie()
            
            liczba = int(input("Podaj liczbę zadań (maksymalnie 5): \n"))

            bufor = f"{liczba_studenta.im_nazw_studenta_lower}_kolokwium.ipynb"

            kolokwia_generator.generuj_kolokwium(bufor, liczba)


            break
        elif wybor == 2:

            liczba = int(input("Podaj liczbę zadań (maksymalnie 5): \n"))

            for i in importowanie_excel.dane.values():

                liczba_studenta.im_nazw_studenta = i[0] + " " + i[1]
                liczba_studenta.zmien_litery_ins()
                liczba_studenta.finalna(liczba_studenta.im_nazw_studenta)
                liczba_studenta.zapis_sprawdz(liczba_studenta.im_nazw_studenta_lower, liczba_studenta.finalna_liczba)
                liczba_studenta.liczby_studentow_wszystkie()


                bufor = f"{liczba_studenta.im_nazw_studenta_lower}_kolokwium.ipynb"

                kolokwia_generator.generuj_kolokwium(bufor, liczba)
              
            break
        else:
            print('Niepoprawne dane, spróbuj ponownie\n')

menu()