class Rectangle:
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __str__(self):
        return f"短形 幅:{self.width} 高さ:{self.height}"
rect = Rectangle(3,5)
print(rect)
print(rect.area())