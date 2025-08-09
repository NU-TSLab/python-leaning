class Book:
    total_books=0

    def __init__(self,title):
        self.title=title
        Book.total_books+=1

book1=Book("ABC")
book2=Book("XYZ")
print(Book.total_books)