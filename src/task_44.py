class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books +=1

book1 = Book("aaa")
book2 = Book("bbb")

print(Book.total_books)