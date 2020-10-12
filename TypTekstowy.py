imie = "Jan"
nazwisko = "Nowak"
# string to tablica znaków więc możemy odwołać się do jej elementów
print(imie[0])
# indeks elementu możemy również określać jako pozycja od końca ciągu
print(imie[-1])
# można również pobrać fragment ciągu (slice) określając jako indeks
# element początkowy i końcowy. Zwróć uwagę na wartość tych indeksów.
print(imie[0] + imie[-2] + imie[4:6])
# można również określic tylko jeden z dwóch indeksów
print(imie + nazwisko[3:])
# inny sposób złączania ciągów
print(imie + " " + nazwisko)
# Elementów ciągu nie można zmieniać więc poniższa instrukcja zwróci
#błąd.
# nazwisko[0] = "P"
# Potwierdzeniem tego, że ciąg tekstowy jej również obiektem jest
#możliwość
# wykonania na nim metod dla tego typu zdefiniowanych. Metoda count()
#zlicza
# ilość wystąpień danego ciągu w wartości przechowywanej przez zmienną.
print(imie.count("z"))
# Co ciekawe w Pythonie możemy wywoływać funkcje dla danego obiektu
#już podczas deklaracji
# co na pierwszy rzut oka może wyglądać dość egzotycznie.
print("Jesteś szalona!".count("a"))
# Potwierdzeniem niezmienności zadeklarowanego stringa może być
#również poniższy kod
print(imie.lower())
print(imie)
# Aby zwrócić długość ciągu tekstowego należy posłużyć się wbudowaną
#funkcją len()
print(len(nazwisko))