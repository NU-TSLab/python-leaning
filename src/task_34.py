people=[{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Doe', 'age': 22}]

nennrei=[a['age'] for a in people]
print(nennrei)

over25=[a['name'] for a in people if a['age']>=25]
print(over25)