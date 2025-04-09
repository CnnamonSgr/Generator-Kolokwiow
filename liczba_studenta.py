'''
To jest moduł odpowiadający za pytanie użytkownika o imię i nazwisko studenta, generowanie liczby studenta oraz tworzenie katalogu z biblioteką
numerów studentów. Odpowiedzialny jest on też za sprawdzanie czy kolokwium danego studenta nie było już wcześniej generowane, pytając użytkownika
o nadpis pliku tekstowego
'''

import os # Potrzebna do stworzenia oddzielnych katalogów

im_nazw_studenta_lower = None
finalna_liczba = 0
im_nazw_studenta = None

def wprowadz_imie():
  """
  Funkcja do pobierania imienia studenta

  Sprawdza różne warianty podanych zmiennych by zmniejszyć ilość potencjialnych błędów
  
  Zwraca imię studenta w formie capitalize
  """
  while True:
    try:
      imie_studenta = input('Podaj imię studenta: ').strip()

      if not imie_studenta:
        raise Exception('Wartość nie może być pusta\n')
      
      if imie_studenta.isdigit():
        raise Exception("Wartość nie może być liczbą\n")

      if not imie_studenta.isalpha():
        raise Exception("Imię zawiera niepożądane znaki (np. spację)\n")
      
      imie_studenta = ''.join(x for x in imie_studenta if x.isalpha())
      
      return imie_studenta.capitalize()
    
    except Exception as e:
      print(e)


def wprowadz_nazwisko():
  """
  Funkcja do pobierania nazwisko studenta

  Sprawdza różne warianty podanych zmiennych by zmniejszyć ilość potencjialnych błędów
  
  Zwraca imię studenta w formie capitalize
  """
  while True:
    try:
      nazwisko_studenta = input('Podaj nazwisko studenta: ').strip()

      if not nazwisko_studenta:
        raise Exception('Wartość nie może być pusta\n')
      
      if nazwisko_studenta.isdigit():
        raise Exception("Wartość nie może być liczbą\n")
      
      if not nazwisko_studenta.isalpha():
        raise Exception("Imię zawiera niepożądane znaki (np. spację)\n")
      
      nazwisko_studenta = ''.join(x for x in nazwisko_studenta if x.isalpha())

      return nazwisko_studenta.capitalize()
    
    except Exception as e:
      print(e)



def wprowadz_imie_nazwisko_stu():
  """Funkcja łącząca imię oraz nazwisko studenta w jedną zmienną"""
  global im_nazw_studenta
  im_nazw_studenta = wprowadz_imie() + " " + wprowadz_nazwisko()
  
  return im_nazw_studenta




def zmien_litery_ins():
  """Funkcja zmienia zmienną 'im_nazw_studenta' w jeden ciąg z tylko małymi literami"""
  global im_nazw_studenta_lower
  im_nazw_studenta_lower = (im_nazw_studenta).lower().replace(" ", "_")

  return im_nazw_studenta_lower



def finalna(im_nazw_studenta):
  """
  Funkcja zwracająca liczbę studenta wyliczona z innej funkcji
  
  im_nazw_studenta --> zmienna wygenerowana z funkcji wprowadz_imie_nazwisko_stu
  """
  global finalna_liczba
  finalna_liczba = liczba_studenta(im_nazw_studenta)

  return finalna_liczba
  


def liczba_studenta(n):
  '''
  Funckja wyznacza liczbę studenta bazowaną na reszcie dzielenia przez 5 sumy 
  wartości jego imienia i nazwiska w formie ascii jako wartości n
  '''
  
  # do reszty z dzielenia dodano 1 by ominąć sytuacji gdzie reszta z dzielenia będzie równa 0
  suma = sum(ord(char) for char in n) % 5 + 1 

  return suma



def tworzenie_katalogu(nazwa_katalogu):
  '''
  Funkcja tworzy katalog w którym umieszczane będą pliki z wynikami liczb studentów
  
  nazwa_katalogu --> nazwa katalogu z liczbami studentów
  '''
  # Ta linia ustala, gdzie znajduje się plik .py w którym obecnie się znajduje (folder)
  sciezka_skryptu = os.path.dirname(os.path.abspath(__file__))

  # Ta linia łączy ścieżkę do katalogu skryptu z nazwą nowego katalogu
  pelna_sciezka = os.path.join(sciezka_skryptu, nazwa_katalogu)

  # Ta linia tworzy katalog pod pełną ścieżką
  os.makedirs(pelna_sciezka, exist_ok=True)

  return pelna_sciezka

# tworzenie katalogu i zapamiętywanie jego ścieżki

sciezka_wyniki = tworzenie_katalogu("biblioteka_liczb_stud")

def student_zapis(im_nazw_studenta_lower, finalna_liczba):
  '''
  Funkcja tworzy plik z imieniem i nazwiskiem studenta oraz wpisuje do niego jego imię i nazwisko razem z liczbą
  
  im_nazw_studenta_lower --> Imię oraz nazwisko studenta z wcześniej urzytej funkcji
  finalna_liczba --> liczba wygenerowana z funkcji przypisana do studenta
  '''

  # Wchodzi do utworzonego wcześniej katalogu i tworzy plik z nazwą studenta 
  pelna_sciezka_do_pliku = os.path.join(sciezka_wyniki, f'{im_nazw_studenta_lower}_test.txt')

  # Otwiera 
  with open(pelna_sciezka_do_pliku, 'w') as f:
    f.write(f"Imię oraz nazwisko studenta: {im_nazw_studenta}, \njego numer --> {finalna_liczba}\n")
  

def zapis_sprawdz(im_nazw_studenta_lower, finalna_liczba):
  '''
  Funkcja sprawdza czy podany plik istnieje, jeżeli tak pyta użytkownika czy go nadpisać
  
  im_nazw_studenta_lower --> Imię oraz nazwisko studenta z wcześniej urzytej funkcji
  finalna_liczba --> liczba wygenerowana z funkcji przypisana do studenta
  '''

  # Zmienna przechowuje ścieżkę którą ma sprawdzać ta funkcja 
  pelna_sciezka_do_pliku = os.path.join(sciezka_wyniki, f'{im_nazw_studenta_lower}_test.txt')

  try:
    with open(pelna_sciezka_do_pliku, 'r'):
      odpowiedz = input(f'Plik ({im_nazw_studenta_lower}_test.txt) już istnieje, czy chcesz go nadpisać? (t/n): ').strip().lower()
      if odpowiedz == "t":
        student_zapis(im_nazw_studenta_lower, finalna_liczba)
        print(f'Plik ({im_nazw_studenta_lower}_test.txt) został nadpisany\n')
        #print(f"Liczbą studenta {im_nazw_studenta_lower} jest: {finalna_liczba}")
      else:
        print(f'Plik ({im_nazw_studenta_lower}_test.txt) nie został nadpisany\n')
  except FileNotFoundError:
    student_zapis(im_nazw_studenta_lower, finalna_liczba)
    print(f"Liczbą studenta {im_nazw_studenta} jest: {finalna_liczba}")


def liczby_studentow_wszystkie():
  """Funkcja łącząca wszystkie pliki z biblioteki liczb w jedno miejsce"""

  sciezka_skryptu = os.path.dirname(os.path.abspath(__file__))
  sciezka_do_pliku = os.path.join(sciezka_skryptu, 'liczby_studentow.txt')

  with open(sciezka_do_pliku, 'w') as wyniki:
    for plik in os.listdir(sciezka_wyniki):
      if plik.endswith('.txt'):
        pelna_sciezka = os.path.join(sciezka_wyniki, plik)
        with open(pelna_sciezka, 'r') as f:
          wyniki.write('======================================================')
          wyniki.write('\n')
          wyniki.write(f.read())
          wyniki.write('======================================================')
          wyniki.write('\n\n')
