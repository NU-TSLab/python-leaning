import csv

class Student:
    def __init__(self, name, score_list):
        self.name=name
        self.score_list=score_list

    def get_average_score(self):
        ave=sum(self.score_list)/len(self.score_list)
        return ave

    def display_score(self):
        average_score=self.get_average_score()
        print(f"{self.name}: 平均点 {average_score:.2f}")

class Grade:
    def __init__(self):
        self.student_list=[]
        self.subject_list=[]

    def get_high_score(self):
        if not self.student_list:
            print("生徒のリストが空です。")
            return

        top_student=max(self.student_list, key=lambda student: student.get_average_score())
        top_score=top_student.get_average_score()
        print(f"最高点の生徒: {top_student.name}, 平均点: {top_score:.2f}")

def load_data_from_csv(file_path):
    grade=Grade()

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader=csv.reader(csvfile)

        headers=next(reader)
        grade.subject_list=headers[1:]  

        for row in reader:
            name=row[0]
            scores=list(map(int, row[1:]))
            student=Student(name, scores)
            grade.student_list.append(student)

    return grade

if __name__ == "__main__":
    file_path = "C:\\Users\\itachi.2590\\python-leaning\\data\\task_56.csv"
    grade=load_data_from_csv(file_path)

    print("教科:", ", ".join(grade.subject_list))
    for student in grade.student_list:
        student.display_score()

    grade.get_high_score()
