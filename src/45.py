class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

book1 = Book("空想科学読本")
book2 = Book("論理回路")
book3 = Book("ドラえもん")
print(Book.total_books)