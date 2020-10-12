spam = 'SPAM ' * 10
print(spam)

szescian = 5 ** 3
print(szescian)

reszta = 12 % 5
print(reszta)

oceny = [1, 2, 3, 4, 5] * 2
print(oceny)

liczba1 = 1
liczba2 = 2
print(liczba1 > liczba2)
print(liczba1 <= liczba2)
print(liczba1 == liczba2)
print(liczba1 != liczba2)


całkowita = 5
rzeczywista = 5.6
rzeczywista = float(56)

print(rzeczywista)
liczba_str = "123"
liczba = int(liczba_str)
print(type(liczba))

a, b = 3, 4

print(b)

imie = "Jan"
nazwisko = "Nowak"
print('-------------------------')

### koniec ciągu ostatni element -1
print(imie[-1])

print(imie[0:6])

print(imie + nazwisko[3:])


print(imie + " " + nazwisko)
print(len(imie))

print("Używamy wersji Python %i" % 3)
print("A dokładniej Python %f" % 3.5)

print("Lubię język {1} oraz {0}".format("Java", "Python"))

year = 2016
event = 'Referendum'
print('Results of the {year} {event}')
print(f'Results of the {year} {event}')
print('AAAAResults of the {0} {1}'.format(year, event))

year = 2016
event = 'Referendum'
f'Results of the {year} {event}'


yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:1.1%}'.format(yes_votes, percentage))

s = 'Hello, world.'
print(type(s))
print(s)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
print(f'The value of x is {x}, and y is {y}...')

print(type(x))

lista = []
lista2 = list()
lista3 = [1, 2, 3]
lista4 = ["a", 5, "Python", 7.8]

print(lista3)

lista3.extend(lista4)
print(lista3)
lista6 = lista3 +lista4

lista.append(6)


class Osoba:
 def __init__(self, imie, nazwisko):
    self.imie = imie
    self.nazwisko = nazwisko


kr = Osoba("Jan", "Nowak")
print("Tą osobą jest {0.imie} {0.nazwisko}".format(kr))
print(f'Tą osobą jest {kr.imie} {kr.nazwisko}')


