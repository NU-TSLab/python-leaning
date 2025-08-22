class Employee:
    def __init__(self):
        self._salary=0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if value < 0:
            print("エラー発生。0以上の給与を入れてください。")
        else:
            self._salary=value

em=Employee()
em.salary=25000
print(em.salary)

em.salary=-1000
print(em.salary)