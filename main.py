from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, klima=True):
        super().__init__(szobaszam)
        self.klima = klima
        self.ar = 8000 if klima else 7000

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, erkely=False):
        super().__init__(szobaszam)
        self.erkely = erkely
        self.ar = 10000 if erkely else 9000

class Szalloda:
    def __init__(self, nev, cim):
        self.nev = nev
        self.cim = cim
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, kezdes_datum, vege_datum):
        self.szoba = szoba
        self.kezdes_datum = kezdes_datum
        self.vege_datum = vege_datum