import csv
class Grade:
    def __init__(self, subject_list):
        self.student_list = []
        self.subject_list = subject_list

    def student(self, student):
        self.student_list.append(student)

    def get_high_score(self):
        student_score = max(self.student_list, key=lambda student: student.get_average_score())
        print(f"最高平均点の人は{student_score.name}, 平均点は{student_score.get_average_score():.2f}点でした。")

class Student:
    def __init__(self, name, score_list):
        self.name = name
        self.score_list = score_list

    def score_list(self):
        return self._score_list

    def score_list(self, value):
        self._score_list = value

    def get_average_score(self):
        return sum(self.score_list) / len(self.score_list) if self.score_list else 0

    def display_score(self):
        average = self.get_average_score()
        print(f"{self.name} の平均点: {average:.2f}")

def load_data_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        subject_list = next(reader)[1:] 
        grade = Grade(subject_list)
        grade.student_list = [Student(row[0], list(map(int, row[1:]))) for row in reader]
    return grade

file_path = './data/task_56.csv'
grade_instance = load_data_from_csv(file_path)
grade_instance.get_high_score()