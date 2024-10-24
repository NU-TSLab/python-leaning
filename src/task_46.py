class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1


book1 = Book("英単語帳")
book2 = Book("レシピ本")
print(Book.total_books)
