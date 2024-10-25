import os
with open('C:\\Users\\itachi.2590\\python-leaning\\data\\sample.txt','w') as file:
    file.write('Hello, World!!')
    file.close()

with open('C:\\Users\\itachi.2590\\python-leaning\\data\\sample.txt','r') as file:
    a=file.read()
    print(a)

os.remove('C:\\Users\\itachi.2590\\python-leaning\\data\\sample.txt')