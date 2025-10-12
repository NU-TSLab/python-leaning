class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def find_top_student(students):
        top_student = max(students, key=lambda student: student.grade).name
        return top_student

students = [Student("太郎", 85), Student("花子", 92), Student("次郎", 78)]
print(Student.find_top_student(students))