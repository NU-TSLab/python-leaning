#辞書のリストを作成する
people = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Doe', 'age': 22}]

#すべての人物の年齢のリストを作成する
ages = [person['age'] for person in people]
print(ages)

#すべての人物の名前のリストを作成する
names = [person['name'] for person in people]
print(names)

'''
[25, 30, 22]
['John', 'Jane', 'Doe']
'''
