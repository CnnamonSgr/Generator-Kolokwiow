'''
Jeden z kluczowych modułów. Przechowuje on wszystkie dostępne zadania (na tą chwilę 5) oraz na ich podstawie tworzy i zapisuje
plik JSON (.ipynb) jako notebook który student otrzymuje jako kolokwium.

'''


import os
import json
import liczba_studenta  # aby mieć dostęp do globalnych zmiennych, np. liczba_studenta.im_nazw_studenta_lower_list
from liczba_studenta import tworzenie_katalogu


# Tworzy katalog na wygenerowane kolokwia
sciezka_kolosy = tworzenie_katalogu("wygenerowane_kolosy")

lista = [
        [
            '',
            'Witaj, znajdujesz się właśnie w programie do programowania. Wierzę że uda ci się napisać odpowiedni program. Właśnie piszę dla ciebie ten tekst abyś mógł wykonać to zadnie. Kto by pomyślał, że w jednym tekście może znaleźć się aż tyle słów, a co za tym idzie liter. Baw się dobrze podczas programowania. Powodzenia.',
            'Później mówiono, że człowiek ten nadszedł od północy; od Bramy Powroźniczej. Szedł pieszo, a objuczonego konia prowadził za uzdę. Było późne popołudnie i kramy powroźników i rymarzy były już zamknięte, a uliczka pusta.',
            'Tetris to komputerowa gra logiczna stworzona przez Aleksieja Pażytnowa i jego współpracowników, Dimitrija Pawłowskiego i Wadima Gieriasimowa. Pojawiła się na rynku po raz pierwszy 6 czerwca 1984 roku w Związku Radzieckim. Jest to jedna z najbardziej znanych gier komputerowych, posiadająca dużą liczbę różnorodnych wariacji i wariantów.',
            'W tym momencie jak to piszę myślę nad tekstem, który mogę tu wstawić. Zgaduję że i tak później zmienimy go, bo nie ma opcji że to przejdzie, ale pomyślimy o tym później, na razie niech zostanie to co tutaj jest, bo lepsze to niż nic!',
            'Cieszę się że czytasz ten tekst i nie masz problemu z rozwiązywaniem zadań. Życzę powodzenia w kolejnych zadaniach i pamiętaj aby nie korzystać z pomocy sztucznej inteligencji.'
        ],
        [
            '',
            'Gr#tul#cj3 r?zw9#z#l3s t? z#d#ni3 p?pr#wn93. C93sz3 s93 z3 p?sw93c9l3s n# n93 wyst#rcz#j#c? duz? cz#su. C93k#w3 9l3 t? z#d#n93 z#j3l? c9 cz#su',
            'D?br# r?b?t#, ud#l? c9 s93 p?pr#wn93 r?zszyfr?w#c t# w9#d?m?sc!',
            'L9tw?! Ojczyzn? m?j#! ty j3st3ś j#k zdr?w93.Il3 c9ę trz3b# c3n9ć, t3n tylk? s9ę d?w93,Kt? c9ę str#c9ł. Dz9ś p9ękn?ść twą w c#ł3j ?zd?b93W9dzę 9 ?p9suję, b? tęskn9ę p? t?b93.',
            'Wbr3w ?b93g?w3j ?p9n99 l#ngust# żyw9 s9ę wyłączn93 ?w?c#m9 m?rz#. Ch?ć gdyby m?gł#, j#dł# by dż3m.',
            'W93cz?r3m prz3d mym d?m3m, wyst#w9ę 3kr#n 9 wyśw93tlę f9lm, c?ś ? mn93 9 ? t?b93, będę l3czył ch?r3 sąs9#dów sny.'
        ],
        [
            '',
            'niebieskich sedanów oraz czerwonych kombi',
            'czerwonych sedanów oraz niebieskich kombi',
            'czarnych sedanów oraz srebrnych kombi',
            'srebrnych sedanów oraz czarnych kombi',
            'niebieskich sedanów oraz srebrnych kombi'     
        ]

    ]
    


def zasady():
    """Funkcja zawierająca zasady dla konkretnego studenta"""

    return f'''# Programowanie, kolokwium
## Zdający - {liczba_studenta.im_nazw_studenta}
**Reguły**,
* prace są samodzielne, można korzystać ze swoich własnych kodów, wykładu, ćwiczeń, książek, manuali, dokumentacji, kursów, itp…
* nie wolno korzystać z cudzych kodów na zasadzie copy-paste oraz z AI - takie zadania otrzymają 0 punktów.

**Uwaga**

Warto testować swoje kody. Brak testów to pierwszy krok do słabej / niezadowalającej oceny z kolokwium. Testować, tzn. po napisaniu programu (kodu) należy go kilkukrotnie uruchomić dla kilku różnych danych wejściowych.

    Zadanie bez testu otrzyma mniej punktów. W treści zadania jest zaznaczone, czy test jest wymagany.

**Uwaga 2**
    
Warto używać porządnych nazw zmiennych oraz komentarzy.
\n

    Powodzenia!'''


def zad_1():
    """Funkcja zawierająca dane do zadania"""

    return f'''

Utwórz plik z tekstem niżej i napisz funkcję która wczytuje plik i zlicza słowa znajdujące się w tekście. Pamiętaj o usunięciu przecinków, kropek 
oraz o zmianie wielkości liter. Wykorzystaj import string oraz string.ascii_lowercase.
P.S nie zapomnij o polskich znakach


Tekst:

*{lista[0][liczba_studenta.finalna_liczba]}*'''


    

def zad_2():
    """Funkcja zawierająca dane do zadania"""

    return f'''

Po przejściu poziomu w pewnej grze zdobywamy zasoby w postaci drewna, kamienia oraz metalu, gdzie drewno jest warte 1 monetę, kamień 2 monety, a metal 5 monet.
Między poziomami znajdujemy się w sklepie i możemy zakupić zasoby na kolejny poziom, jednak sklepikarz nie potrafi na szybko przeliczyć przyniesione materiały na monety.

Napisz funkcję która pomoże sklepikarzowi wydać resztę, bądź stwierdzić czy przyniesiono wystarczająco monet gdy bohater przyszedł kupić:
2 mikstury, każda warta {liczba_studenta.finalna_liczba} monet(y)
broń wartą {liczba_studenta.finalna_liczba * 3 + 7} monet(y)
zbroje wartą {liczba_studenta.finalna_liczba * 2 + 1} monet(y)
3 bochenki chleba każdy wart 2 monety.

Przetestuj dla:
- 4szt metalu, 3szt kamienia, 6szt drewna
- 5szt metalu, 1szt kamienia, 10szt drewna
- 8szt metalu, 4szt kamienia, 5szt drewna'''

    

def zad_3():
    """Funkcja zawierająca dane do zadania"""

    return f'''

Antek postanowił zmienić swoje życie na lepsze więc zaczął robić pompki i rozpoczął naukę programowania. 
Przez miesiąc (30dni) codziennie zwiększał ilość pompek o {liczba_studenta.finalna_liczba+3} oraz uczył się {liczba_studenta.finalna_liczba+1} razy dłużej 
niż dnia poprzedniego. Zaczął od {liczba_studenta.finalna_liczba} pompek i od 5 minut nauki.

Napisz 2 funkcje (iteracyjną i rekurencyjną) które policzą ile w każdym dniu wykonał pompek oraz ile czasu się uczył. 
Oblicz również sumę wykonanych pompek oraz sumę czasu spędzonego na programowaniu.
'''


def zad_4():
    """Funkcja zawierająca dane do zadania"""

    return f'''

Ktoś zaszyfrował poniższa wiadomość! Napisz kod który pomoże w rozszyfrowaniu zdanie i stworzy z niego wiadomość (pamiętaj o dużych literach).

Wszystkie litery zostały pozamieniane na konkretne znaki:

- a -> #
- e -> 3
- i -> 9
- o -> ?

Wiadomość:

*{lista[1][liczba_studenta.finalna_liczba]}*'''

def zad_5():
     """Funkcja zawierająca dane do zadania"""

     return f'''
    
Pewna wytwórnia tablic rejestracyjnych dostała zlecenie na stworzenie 100 przykładowych tablic dla 100 różnych samochodów. Różniły się od siebie kolorem
lakieru oraz nadwoziem: część z nich to były kombi, a druga część to sedany. Wytwórnia, by na podstawie samych tablic zdołała zidentyfikować kolor oraz typ 
nadwozia, stworzyła specjalny system rozpoznawania, w którym to typ nadwozia był definiowany przez to, czy suma cyfr na tablicy była parzysta bądź nie, a kolor 
był resztą z dzielenia przez 4 numerów ascii liter tych tablic, gdzie reszta: 1 = czerwony, 2 = niebieski, 3 = srebrny, brak reszty (0) = czarny. 

Rejestracje samochodów zostały podane niżej. Na ich postawie określ ile jest {lista[2][liczba_studenta.finalna_liczba]}. Pamiętaj by do wyniku NIE uwzględnić numer
ascii spacji. 

{rejestracje()}'''

def rejestracje():
    """Funkcja zawierająca dane do zadania"""

    return'''rejestracje = [WZ 12345,
PO 54321,
KR 4573X,
DW 3489Y,
GD 8347E,
WA 6712S,
EL 1203T,
LU 8423P,
BI 4392L,
ZS 7392A,
RA 1284V,
WE 2345R,
CB 9920K,
NE 3030H,
TK 1830G,
OP 4010M,
WP 3921J,
NO 4736C,
DL 1829B,
PK 8384D,
WX 7481F,
KK 5003Z,
LB 9110N,
LD 6481X,
WL 2395Y,
EZG 4734A,
SK 8392V,
RZ 4839T,
GL 7284R,
FG 9304E,
ST 2938P,
RJA 8292M,
SZA 1039L,
PL 9043W,
SZ 5647G,
KT 4382S,
SZY 9382H,
RMI 2284C,
KMY 8392B,
PZ 2834D,
KRK 3920F,
SCI 8391Z,
TBU 2849X,
DWR 9182Y,
LZA 8294A,
WLS 1039V,
LC 3401T,
WGM 2381R,
EPI 4398E,
GPU 3829P,
NBA 2937M,
CBR 2938L,
GSP 1827W,
CTR 9382G,
ZKA 2819S,
EWI 3928H,
NLI 3748C,
PWA 9381B,
SMY 3728D,
FGW 9382F,
SWD 4729Z,
KTA 2893X,
KGR 9847Y,
PKO 8372A,
POS 2983V,
SGL 3928T,
KBR 3928R,
WMA 9382E,
CNA 2829P,
GWE 9384M,
RSA 9384L,
POB 8327W,
KLI 2849G,
NEL 9382S,
PSE 9372H,
LHR 8473C,
KBC 9381B,
ZPL 2837D,
KRA 8372F,
PSZ 9382Z,
STA 8492X,
SRC 8392Y,
EBE 8372A,
WPL 9382V,
WPN 8374T,
WKZ 9381R,
WWL 4738E,
WWY 9382P,
WND 9273M,
KNS 3839L,
TSK 9384W,
SZD 2837G,
KOS 9384S,
SB 2848H,
CCH 9382C,
WBR 8372B,
KSU 9381D,
WS 4738F]
'''
    


def zapisz_plik(notebook, nowa_nazwa):
     """
     Zapisuje obiekt notebook (JSON) do pliku w katalogu wygenerowanych kolokwiów.
     
     notebook --> zawartość tworzonego pliku .json 

     nowa_nazwa --> nazwa danego pliku
     """
     pelna_sciezka = os.path.join(sciezka_kolosy, nowa_nazwa)
     with open(pelna_sciezka, "w", encoding="utf-8") as f:
         json.dump(notebook, f, indent=1, ensure_ascii=False)

liczba = None

def liczba_zadan(liczba):
    """
    Funkcja wyliczająca ile zadań pobrać z listy by z nich utworzyć kolokwium, oraz
    wrzucenie tych zadań do odpowienich list w celu ich późniejszego wykorzystania

    liczba --> Wybrana wcześniej liczba zadań potrzebna w celu wyliczenia ilości zadań do pobrania
    """
    while True:
        try:            
            if liczba > 5:
                raise Exception('Wartość podanych zadań nie może być większa od 5')
                
            lista_komorek = []

            komorka_zasady = {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    zasady()
                ]
            }

            lista_komorek.append(komorka_zasady)

            zadania = [zad_1(), zad_2(), zad_3(), zad_4(), zad_5()]

            for i in range(1, liczba + 1):

                # Komórka markdown
                komorka_markdown = {
                    'cell_type': 'markdown',
                    'metadata': {},
                    'source': [
                        f'**Zadanie {i}:**\n',
                        f"\n{zadania[i - 1]}"
                    ]
                }

                # Komórka code
                komorka_code = {
                    "cell_type": "code",
                    "metadata": {},
                    "execution_count": None,
                    "outputs": [],
                    "source": [
                        f'#kod_zadanie_{i}'
                    ]
                }
                
                # Dodawanie dwóch komórek do listy (najpierw markdown, potem code)
                lista_komorek.append(komorka_markdown)
                lista_komorek.append(komorka_code)

            return lista_komorek

        except Exception as e:
            print(e)
            continue
            


def generuj_kolokwium(bufor, liczba):
    """
    Główna funkcja pliku służąca do połaczenia wszystkich komórek i uruchomienia
    funkcji generującą pliki

    bufor --> nazwa konkretnego pliku kolokwium

    liczba --> Liczba zadań wybrana w pliku menu.py
    """
    cells = liczba_zadan(liczba)

    notebook = {
        'cells': cells,
        'metadata': {},
        'nbformat': 4,
        'nbformat_minor': 5
    }

    zapisz_plik(notebook, bufor)




