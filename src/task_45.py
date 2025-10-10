class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return f"矩形　幅: {self.width}, 高さ: {self.height}"
    
r1 = Rectangle(5, 10)
r2 = Rectangle(8, 4)

print(r1)
print(r1.area())
print(r2)
print(r2.area())