class Book:
    total_books=0
    def __init__(self,title):
        self.title=title
        self.__class__.total_books +=1

book1=Book("物理教科書")
book2=Book("透明な螺旋")
print(Book.total_books)
