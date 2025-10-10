class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

def find_top_student(students):
    return max(students, key = lambda student: student.grade).name

students = [Student("Ryoma", 100), Student("Reo", 0), Student("Kenshin", 3)]
top_student = find_top_student(students)
print(top_student)