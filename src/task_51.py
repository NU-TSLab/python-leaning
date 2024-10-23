import os

with open('./data/sample.txt', 'w') as file:
    file.write('Hello, World!')

with open('./data/sample.txt', 'r') as file:
    content = file.read()
    print(content)

os.remove('./data/sample.txt')