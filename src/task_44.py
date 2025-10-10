class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

man = Book("男塾　第一巻")
goat = Book("ONE PIECE　第一巻")
orz = Book("ムヒョとロージがあーだこーだ　第一巻")

print(Book.total_books)