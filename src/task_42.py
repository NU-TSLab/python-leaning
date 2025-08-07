class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

def find_top_student(selfstudents):
    return max(students, key=lambda student: student.grade).name
    
students = [Student("Alice", 90), Student("Bob", 80), Student("Charlie", 70)]
top_student = find_top_student(students)
print(top_student)