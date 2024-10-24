class Employee:
    def __init__(self):
        self.salary = 0
    
    @property  #@propertyはメソッドを属性として扱うことができる
    def salary(self):
        return self.__salary
    
    @salary.setter  #@property.setterは属性に値を設定することができる
    def salary(self, value):
        if value < 0:
            print("給料は0以上にしてください")
        else:
            self.__salary = value

emp = Employee()
emp.salary = 1000
print(emp.salary)
emp.salary = -1000

#1000
#給料は0以上にしてください