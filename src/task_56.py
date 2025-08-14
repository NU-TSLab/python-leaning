import csv
class Grade:
    def __init__(self,student_list,subject_list):
        self.student_list=student_list
        self.subject_list=subject_list
    def get_high_score(self):
        ave_topscore_student=max(self.student_list,key=lambda student:student.get_average_score())
        ave_topscore=ave_topscore_student.get_average_score()
        print(f'最高平均点の生徒：{ave_topscore_student.name} 生徒の平均点：{ave_topscore}')
class Student:
    def __init__(self,name,score_list):
        self.name=name
        self.score_list=score_list
    def get_average_score(self):
        return sum(self.score_list)/len(self.score_list)
    def display_score(self):
        average=self.get_average_score()
        print(f'{self.name}の平均点：　{average}点')
student_list=[]
subject_list=[]
with open('./data/task_56.csv',encoding='utf-8')as csvfail:
    reader=csv.reader(csvfail)
    header=next(reader)
    subject_list=header[1:]
    for row in reader:
        name=row[0]
        score=list(map(int,row[1:]))
        student=Student(name,score)
        student_list.append(student)
grade=Grade(student_list,subject_list)
for student in grade.student_list:
    student.display_score()
grade.get_high_score()