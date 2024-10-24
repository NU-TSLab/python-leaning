class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

book1 = Book("时代广场的蟋蟀")
book2 = Book("钢铁是怎样炼成的")
print(Book.total_books)

#2