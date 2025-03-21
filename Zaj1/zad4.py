class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania) -> None:
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def opis(self):
        return f"{self.tytul} - {self.autor} ({self.rok_wydania})"
    
class Ebook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, rozmiar_pliku) -> None:
        super().__init__(tytul, autor, rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku

    def opis(self):
        return f"{super().opis()} - {self.rozmiar_pliku} MB"
    
class Audiobook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, czas_trwania) -> None:
        super().__init__(tytul, autor, rok_wydania)
        self.czas_trwania = czas_trwania

    def opis(self):
        return f"{super().opis()} - {self.czas_trwania} min"
        

if __name__ == "__main__":

    ksiazka = Ksiazka("Hobbit", "J.R.R. Tolkien", 1937)
    ebook = Ebook("Władca Pierścieni", "J.R.R. Tolkien", 1954, 10)
    print(ebook.opis())
    audiobook = Audiobook("Harry Potter", "J.K. Rowling", 1997, 600)
    print(audiobook.opis())
    print(ksiazka.opis())