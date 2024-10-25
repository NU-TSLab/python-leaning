class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"矩形 幅: {self.width}, 高さ: {self.height}"

rect = Rectangle(4, 5)
print(rect)  # 矩形 幅: 4, 高さ: 5
print(rect.area())  # 20