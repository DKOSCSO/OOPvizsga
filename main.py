from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
    @abstractmethod
    def megtekintes(self):
        pass
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, ar=80000)

    def megtekintes(self):
        return f"Egyágyas szoba #{self.szobaszam}, Ára: {self.ar} Ft"

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, ar=100000)

    def megtekintes(self):
        return f"Kétágyas szoba #{self.szobaszam}, Ára: {self.ar} Ft"
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                for foglalas in self.foglalasok:
                    if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                        return "A szoba már foglalt, válasszon másik időpontot."

                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return f"Foglalás sikeres. Ára: {szoba.ar} Ft."

        return "Nincs ilyen szobaszám."

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return "Foglalás lemondva."

        return "Nincs ilyen foglalás"

    def listaz_foglalasok(self):
        if not self.foglalasok:
            return "Nincsenek foglalások."

        result = "Foglalások:\n"
        for foglalas in self.foglalasok:
            result += f"{foglalas.szoba.megtekintes()}, Dátum: {foglalas.datum}\n"

        return result

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

szalloda = Szalloda(nev="Hotel Python")

szalloda.add_szoba(EgyagyasSzoba(szobaszam=111))
szalloda.add_szoba(KetagyasSzoba(szobaszam=121))
szalloda.add_szoba(EgyagyasSzoba(szobaszam=201))

szalloda.foglalas(szobaszam=111, datum=datetime(2023, 12, 10))
szalloda.foglalas(szobaszam=121, datum=datetime(2023, 12, 30))
szalloda.foglalas(szobaszam=201, datum=datetime(2023, 12, 25))
szalloda.foglalas(szobaszam=111, datum=datetime(2024, 12, 10))
szalloda.foglalas(szobaszam=121, datum=datetime(2024, 12, 30))

print("Üdvözöljük a Hotel Pythonban!")
nev = input("Hogyan szólíthatjuk?\nKérem írja be a nevét:\n")
print("Kedves " + nev + "\nKérjük válasszon az alábbi menüpontok közül:")

while True:
    print("\nVálasszon műveletet:")
    print("1. Szobák megtekintése")
    print("2. Szobák foglalása")
    print("3. Foglalás lemondása")
    print("4. Foglalások listázása")
    print("0. Kilépés")

    valasztas = input("Választás: ")

    if valasztas == "1":
        print("\nSzobák:")
        for szoba in szalloda.szobak:
            print(szoba.megtekintes())
    elif valasztas == "2":
        szobaszam = int(input("Adja meg a szobaszámot: "))
        datum = datetime.strptime(input("Adja meg az érkezés dátumát (YYYY-MM-DD): "), "%Y-%m-%d")
        print(szalloda.foglalas(szobaszam, datum))
    elif valasztas == "3":
        szobaszam = int(input("Adja meg a szobaszámot: "))
        datum = datetime.strptime(input("Adja meg a lemondás dátumát (YYYY-MM-DD): "), "%Y-%m-%d")
        print(szalloda.lemondas(szobaszam, datum))
    elif valasztas == "4":
        print(szalloda.listaz_foglalasok())
    elif valasztas == "0":
        break
    else:
        print("Érvénytelen választás. Kérem, válasszon újra.")