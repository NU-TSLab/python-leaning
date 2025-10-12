class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return f"短形 幅：{self.width}, 高さ：{self.height}"

rect = Rectangle(5, 10)
print(rect)
print("面積:", rect.area())