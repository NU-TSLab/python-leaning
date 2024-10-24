class Employee:
    def __init__(self):
        self._salary = 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("給与は0以上でなければなりません")
        else:
            self._salary = value

emp = Employee()
emp.salary= 100000
print(emp.salary)
emp.salary = -100