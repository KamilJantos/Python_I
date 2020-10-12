# tworzenie słownika
slownik = {}
slownik = dict([("jeden", 1), ("dwa", 2), ("trzy", 3)])
slownik = dict(jeden=1, dwa=2, trzy=3)
slownik = dict({"jeden": 1, "dwa": 2, "trzy": 3})
slownik = {'jeden': 1, "dwa": 2, "trzy": 3}
print(slownik["jeden"])
# sprawdzenie czy klucz jest w słowniku czy nie
print("jeden" in slownik)
# wypisanie wszystkich kluczy
print(slownik.keys())
# wypisanie wszystkich wartości
print(slownik.values())
# można również sprawdzić czy klucz występuje w słowniku
# w przedstawiony poniżej sposób, ale jest on wolniejszy
print("jeden" in slownik.keys())
# dodanie elementu do słownika
slownik["cztery"] = 4
print(slownik.keys())