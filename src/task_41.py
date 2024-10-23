class car:
    def __init__(self,make,year):
        self.make=make
        self.year=year

    def car_info(self):
        return f"{self.make}の車、年式：{self.year}" 

c=car("ジープ",2003)
print(c.car_info())   #ジープの車、年式：2003    