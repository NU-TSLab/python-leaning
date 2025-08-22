class Book:
    total_books=0

    def __init__(self,title):
        self.title=title
        Book.total_books += 1

book1=Book("Dobutsu")
print(Book.total_books)

book2=[Book("Yukie"),Book("Mari")]
print(Book.total_books)