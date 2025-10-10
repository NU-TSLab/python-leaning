class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def car_info(self):
        return f"{self.make}の車、年式：{self.year}"
    
c = Car("TOYOTA", 2004)
print(c.car_info())