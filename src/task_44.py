class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


def find_top_student(students):
    return max(students, key=lambda student: student.grade).name


students = [Student("佐藤", 80), Student("山田", 60), Student("田中", 30)]
top_student = find_top_student(students)
print(top_student)
