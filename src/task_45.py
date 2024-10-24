class Rectangle:
    def __init__(self, width, heigt):
        self.width = width
        self.heigt = heigt

    def area(self):
        return self.width * self.heigt
    
    def __str__(self):
        return f"短幅 幅 : {self.width}, 高さ : {self.heigt}"

rect = Rectangle(5, 6)
print(rect)
print(rect.area())