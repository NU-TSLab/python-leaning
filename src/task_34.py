# 辞書の配列を作成
people = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Doe', 'age': 22}]

# 1. すべての人物の年齢のリストを作成する
ages = [person['age'] for person in people]
print(ages)  # [25, 30, 22]

# 2. 25歳以上の人物の名前をリストにして出力する
names_over_25 = [person['name'] for person in people if person['age'] >= 25]
print(names_over_25)  # ['John', 'Jane']