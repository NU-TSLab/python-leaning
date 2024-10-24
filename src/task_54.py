import shutil

with open('./data/source.txt','w') as file:
    file.write('abc')

shutil.copy('./data/source.txt', './data/destination.txt')
print('コピー完了')