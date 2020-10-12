#ZAD1
a = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
print(a)


def funkcja(litera1, litera2):
    licznik1 = 0
    licznik2 = 0

    for i in range(0, len(a)):
        if a[i] == litera1:
            licznik1 += 1
        if a[i] == litera2:
            licznik2 += 1

    print("W tekscie jest {0} liter {1} oraz {2} liter {3}".format(licznik1, litera1, licznik2, litera2))

#ZAD2

print("Podaj swoje imię: ")
imie = input()
print("Podaj swoje nazwisko: ")
nazwisko = input()

litera1 = imie[2]
litera2 = nazwisko[3]

funkcja(litera1, litera2)

#ZAD3
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nowaLista = []
nowaLista1 = []

for i in range(5, len(lista)):
    nowaLista.append(lista[i])

for i in range(5, 9):
    nowaLista1.append(lista[i])

print(len(lista))

for i in range(0, len(lista) // 2):
    lista.pop(len(lista) - 1)


print("pierwsza lista: ", lista)
print("druga lista: ", nowaLista)
print("trzecia lista: ", nowaLista1)
#ZAD4
lista.extend(nowaLista)
lista.insert(0, 0)
kopia = lista.copy()
kopia.reverse()
print(kopia)

