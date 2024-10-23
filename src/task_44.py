class Book:
    total_books = 0
    def __init__(self , title):
        self.title = title
        Book.total_books = Book.total_books + 1

Book("頭いい本")
Book("まんが")
print(Book.total_books)