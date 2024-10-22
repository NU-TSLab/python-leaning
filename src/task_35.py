num_dic = [{'name': 'John', 'age': 25}, {
    'name': 'Jane', 'age': 30}, {'name': 'Doe', 'age': 22}]
age_all = [human['age'] for human in num_dic]
print(age_all)
age_over25 = [human['name'] for human in num_dic if human['age'] >= 25]
print(age_over25)
