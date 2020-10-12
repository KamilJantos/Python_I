# inicjalizacja zbiorów
klasa = {"Marek", "Janek", "Ania", "Ewa", "Marek", "Ania"}
print(klasa) # duplikatów już nie ma
# a teraz zbiór znaków ze stringa
czar = set("czabunagunga")
print('---------------')
print(czar)
print('---------------')
inny_czar = set("abrakadabra")
print(inny_czar)
print(czar - inny_czar) # są w czar, ale nie ma w inny_czar
print(czar.difference(inny_czar)) # to samo, ale inaczej
print('---------------')
print(inny_czar - czar) # to nie to samo, jak wiadomo z teorii
print('---------------')
print(czar | inny_czar) # znaki w czar lub inny_czar lub obu
print(czar & inny_czar) # przecięcie czyli część wspólna
print(czar.intersection(inny_czar)) # można tak
print(czar ^ inny_czar) # różnica symetryczna