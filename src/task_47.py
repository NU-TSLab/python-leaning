class Employee:
    def __init__(self):
        self._salary = 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("‹‹—^‚Í0ˆÈã‚Å‚È‚¯‚ê‚Î‚È‚è‚Ü‚¹‚ñ")
        else:
            self._salary = value

emp = Employee()
emp.salary = 50525
print(emp.salary)
emp.salary = -100