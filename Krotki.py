# tworzenie krotki
krotka = (1, 2, "Jacek", "ma")
krotka_liczb = krotka[:2]
print(krotka_liczb)
krotka_stringow = krotka[2:]
print(krotka_stringow)
nowa_krotka = tuple()
najnowsza_krotka = tuple([1, 2, 3])
# można również rzutować typy krotka - lista
lista = [1, 2, "Ala", "też", "ma"]
krotka_z_listy = tuple(lista)
nowa_lista = list(krotka_z_listy)
# krotki mogą być zagnieżdżane
duza_krotka = krotka_stringow, krotka_liczb, tuple(nowa_lista)
print(duza_krotka)
# a jeżeli zagnieździ się listę w krotce …
listokrotka = krotka_z_listy, lista
# to nadal możemy modyfikować elementy listy
listokrotka[1][0] = 0
print(listokrotka)
# pakowanie krotki (tuple packing)
t = 5, 6, 7
print(t)
x, y, z = t
# i rozpakowywanie krotki (tuple unpacking)
# inny sposób łączenia zmiennych różnego typu w string
print("x = " + str(x))
print("y = " + repr(y))
print("z = " + str(z))

e = 1, 2, 3
print(e)

a, b, c = e

print(a, b, c)