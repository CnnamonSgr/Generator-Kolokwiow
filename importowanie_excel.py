'''
Moduł korzystający z biblioteki pandas, wyszukuje plik typu excel oraz na jego
podstawie wyodrębnia trzy kolumny: imię, nazwisko oraz indeks. Dane te później
są wykorzystywane przy wielorazowym generowaniu kolokwiów.
'''
 
import pandas as pd

dfs = pd.read_excel("imiona.ods")  # Wczytanie pliku

nr_indeks = dfs['Nr indeksu']
imiona = dfs['Imię']
nazwiska = dfs['Nazwisko']

dane = {}

# Iterujemy po wszystkich wierszach
for i in range(len(dfs)):

    # imiona = dfs["Imię"].head() <-- ogranicza do 5 pierwszych kolumn
    # nazwiska = dfs["Nazwisko"].head() <-- ogranicza do 5 pierwszych kolumn
    # indeksy = dfs["Nr indeksu"].head() <-- ogranicza do 5 pierwszych kolumn

    indeks = nr_indeks.iloc[i]
    imie = imiona.iloc[i]
    nazwisko = nazwiska.iloc[i]

    # Tworzymy klucz słownikowy na podstawie indeksu
    dane[str(indeks)] = (imie, nazwisko)





