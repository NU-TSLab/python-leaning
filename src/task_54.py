import shutil

with open('C:\\Users\\itachi.2590\\python-leaning\\data\\source.txt', 'w') as file:
    file.write('This is a source file.')

shutil.copyfile('C:\\Users\\itachi.2590\\python-leaning\\data\\source.txt', 'C:\\Users\\itachi.2590\\python-leaning\\data\\destination.txt')
print('コピー完了')