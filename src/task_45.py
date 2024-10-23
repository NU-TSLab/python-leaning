class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return f"矩形の幅{self.width},高さ{self.height}"
rectangle = Rectangle(20,30)
print(rectangle.area())
print(rectangle.__str__())