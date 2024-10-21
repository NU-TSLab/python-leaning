n = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Doe', 'age': 22}]
ages = [m['age'] for m in n]
print(ages)
names = [m['name'] for m in n if(m['age'] >= 25)]
print(names)