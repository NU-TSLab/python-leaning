class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    
def find_top_student(students):
        return max(students, key = lambda student: student.grade).name

students = [Student("Eugeo", 60), Student("Alice", 90), Student("Cardinal", 100)]
result = find_top_student(students)
print(result)