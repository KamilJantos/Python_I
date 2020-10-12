lista = []
lista2 = list()
lista3 = [1, 2, 3]
lista4 = ["a", 5, "Python", 7.8]
lista5 = [lista3, lista4]
print(lista5)


lista3.extend(lista4)
print(lista3)
# lub w prostszy sposób
lista6 = lista3 + lista4
print(lista6)

lista7 = [7, 9, 3, 1]
print('--------------------')
print(lista7)
posortowana = lista7.sort()
print(lista7)
print(posortowana)
print('--------------------')
# wstawianie i usuwanie elementów listy
skala = [1, 2, 3, 4, 5]
# dodawanie elementu na końcu listy
skala.append(6)
print(skala)
# znany już jest sposób odwoływania się do elementu listy poprzez
# indeks więc można wartości listy ustawiać w ten sposób, ale
# nie da się wstawić wartości na indeksie, który nie istnieje
####skala[6] = 7
# zostanie zwrócony błąd IndexError: list assignment index out of
# range ale można zrobić to np. tak
skala[6:] = [7]
# lub tak
skala[len(skala):] = [7]
# alternatywnym sposobem jest wywołanie metody insert
skala.insert(6, 7)
print(skala)
# usuwamy element z końca listy co powoduje, że z wykorzystaniem
# tych metod osiągamy funkcję stosu
skala.pop()
print(skala)
# pop może również przyjmować indeks elementu do usunięcia.
# Metoda pop zwraca również wartość elementu usuwanego
skala.pop(2)
print(skala)


