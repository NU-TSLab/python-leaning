class Car:
    def __init__(self,make,yera):
        self.make = make
        self.year = yera
    
    def car_info(self):
        print(f"{self.make}の車、年式：{self.year}")

car1 = Car("トヨタ",2020)
car1.car_info()