class Employee:
    def __init__(self):
        self.salary = 0
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,value):
        if value < 0:
            print("給与は0以上でなければなりません")
        else:
            self._salary = value


employee = Employee()
employee.salary = 1240
print(employee.salary)
employee.salary = -1 