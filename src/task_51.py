import os


with open('./data/sample.txt', 'w') as file:
    file.write('Hello, World! 你好，世界！')


with open('./data/sample.txt', 'r') as file:
    content = file.read()
    print(content)


os.remove('./data/sample.txt')