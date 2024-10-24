class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    #def introduce(self):
        #return f"{self.name}{self.grade}"

students_list=[
    Student("Taro",20),
    Student("JIro",90),
    Student("Saburo",56)
]

#print(students_list[0].introduce())  
#print(students_list[1].introduce())  
#print(students_list[2].introduce())  

def find_top_student(students_list):

     #def get_grade(student):
     #return student.grade
#top_student = max(students_list, key=get_grade)
#　　　　　　　　　　　↓
    top_student = max(students_list, key=lambda student: student.grade)
   
    return top_student.name  

top_student_name = find_top_student(students_list)
print (top_student_name )
