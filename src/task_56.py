import csv

class Student:
    def __init__(self,name,score_list):
        self.name=name
        self.score_list=score_list

    def get_average_score(self):
        return sum(self.score_list)/len(self.score_list)
    
    def display_score(self):
        avarage=self.get_average_score()
        print(f"生徒：{self.name}，平均点：{avarage:.2f}点")

class Grade:
    def __init__(self,subject_list):
        self.student_list=[]
        self.subjevt_list=subject_list

    def add_student(self,student):
        self.student_list.append(student)

    def get_high_score(self):
        highest_ave_student=max(self.student_list,key=lambda student:student.get_average_score())
        highest_ave=highest_ave_student.get_average_score()
        print(f"平均点が最も高い生徒：{highest_ave_student.name}，平均点：{highest_ave:.2f}")

subject_list=[]
grade=None
with open('./data/task_56.csv',newline='',encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    for i,row in enumerate(reader):
        if i==0:
            subject_list=row[1:]
            grade=Grade(subject_list)
        else:
            name=row[0]
            score_list=list(map(int,row[1:]))
            student=Student(name,score_list)
            grade.add_student(student)

grade.get_high_score()