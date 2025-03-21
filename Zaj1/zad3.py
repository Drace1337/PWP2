class Osoba:

    def __init__(self, imie, nazwisko, wiek) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}"
    
class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja) -> None:
        super().__init__(imie, nazwisko, wiek)
        self.stanowisko = stanowisko
        self.pensja = pensja

    def info_o_pracy(self):
        return f"Pracuję jako {self.stanowisko}, zarabiam {self.pensja} zł"
    
class Manager(Pracownik):

    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja) -> None:
        super().__init__(imie, nazwisko, wiek, stanowisko, pensja)
        self.pracownicy = []

    def przedstaw_sie(self):
        return f"{super().przedstaw_sie()}. Pracuje dla mnie {len(self.pracownicy)} pracownik/ów." 
    
    def dodaj_pracownika(self, pracownik):
        self.pracownicy.append(pracownik)

if __name__ == "__main__":

    osoba = Osoba("Jan", "Kowalski", 30)
    print(osoba.przedstaw_sie())

    pracownik = Pracownik("Adam", "Nowak", 25, "programista", 4000.0)
    pracownik.pensja = 5000.0
    print(pracownik.przedstaw_sie())
    print(pracownik.info_o_pracy())

    manager = Manager("Anna", "Wiśniewska", 35, "kierownik", 10000.0)
    print(manager.przedstaw_sie())
    manager.dodaj_pracownika(pracownik)
    print(manager.przedstaw_sie())
    print(manager.info_o_pracy())