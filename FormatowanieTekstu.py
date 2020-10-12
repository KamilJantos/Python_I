# formatowanie znane z Pythona 2.x
wyznanie = "Lubię %s" % "Pythona"
print(wyznanie)
wonsz = "Python"
print("Lubię %sa" % wonsz)
print("Lubię %s oraz %sa" % ("Pythona", wonsz))
# %s oznacza, że w miejsce tego znacznika będzie podstawiany ciąg tekstowy
# %i - to liczba całkowita
# %f - liczba rzeczywista lub inaczej zmiennoprzecinkowa
# %x lub #X - liczba całkowita zapisana w formie szesnastkowej
print("Używamy wersji Python %i" % 3)
print("A dokładniej Python %f" % 3.5)
print("Chociaż lepiej to zapisać jako Python %.1f" % 3.5)
print("A kolejną glówną wersją Pythona może być wersja %.4f" % 3.6666)
print("A może będzie to wersja %.1f ?" % 3.6666)
print("A może jednak %.f ?" % 3.6666)
wersja = 4
print("A %i w systemie szesnastkowym to %X" % (wersja, wersja))
print("A %i * %i szesnastkowo daje %X" % (wersja, wersja, wersja*wersja))
# Chociaż możliwości przy korzystaniu z mechanizmów powyżej są spore,
# to i kilka wad się również znajdzie. Trzeba pilnować zarówno liczby argumentów jak
# i ich kolejności. Konieczne jest powielanie tej samej zmiennej jeżeli kilka
# razy jest wykorzystywana w formatowanym ciągu. Spójrzmy na inne możliwości.
print("Lubię %(jezyk)s" % {"jezyk": "Pythona"})
print("Lubię %(jezyk)s a czy Ty lubisz %(jezyk)s ?" % {"jezyk": "Pythona"})
# wadą jest dość duża ilość dodatkowego kodu do napisania, ale nazwy zmiennych
# w ciągu pozwalają na ich szybką identyfikację i wielokrotne wykorzystanie w
# dowolnej kolejności
# poniżej kolejny sposób
print("Lubię język {1} oraz {0}".format("Java", "Python"))
# w nowej wersji języka Python możliwe jest również odwoływanie się do elementów
#kolekcji lub pól klasy
class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
kr = Osoba("Jan", "Nowak")
print("Tą osobą jest {0.imie} {0.nazwisko}".format(kr))
