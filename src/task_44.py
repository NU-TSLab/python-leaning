class Book:
    total_book=0
    def __init__(self,title):
        self.title=title
        Book.total_book+=1
book1=Book("Python入門")
book2=Book("データサイエンス入門")
print(Book.total_book)