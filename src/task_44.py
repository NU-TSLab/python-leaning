class Book:
    total_books=0

    def __init__(self,title):
        self.title=title
        Book.total_books+=1

book1=Book("abcde")
book2=Book("fghij")
book3=Book("klmno")
print(Book.total_books)