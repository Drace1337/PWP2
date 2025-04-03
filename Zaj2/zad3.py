class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, ISBN: str) -> str:
        if ISBN in self.books.keys():
            return self.books.get(ISBN)
        else:
            return None
        
if __name__ == "__main__":
    book1 = Library({"12314":"Władca Pierścieni"})
    print(book1.find_book("3124"))
    print(book1.find_book("12314"))