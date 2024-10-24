class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def car_info(self):
        return f"{self.make}の車、年式：{self.year}"


car = Car("ベンツ", 2018)
print(car.car_info())
