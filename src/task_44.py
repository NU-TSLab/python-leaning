class Book:
    total_books = 0

    def __init__(self,title):
        self.title = title
        Book.total_books += 1

book1 = Book("広辞苑")
book2 = Book("星を編む")
book3 = Book("ドラえもん")
print(Book.total_books)