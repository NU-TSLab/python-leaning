import csv


class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)


class Grade:
    def __init__(self, subject_list):
        self.subject_list = subject_list
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_high_score(self):
        top_student = max(self.students, key=lambda s: s.get_average_score())
        print(f'平均が最高得点の生徒は {top_student.name}、平均点は {
              top_student.get_average_score():.2f}点')


with open('./data/task_56.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    subject_list = next(reader)[1:]
    grade = Grade(subject_list)

    for row in reader:
        name = row[0]
        scores = list(map(int, row[1:]))
        grade.add_student(Student(name, scores))

grade.get_high_score()
