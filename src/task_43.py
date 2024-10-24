class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

def find_top_student(students):
    return max(students, key=lambda student: student.grade).name

students = [Student("Marverick", 91), Student("Goose", 87), Student("Iceman",90)]
top_student = find_top_student(students)
print(top_student)