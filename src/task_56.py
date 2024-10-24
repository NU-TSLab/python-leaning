import shutil

with open('./data/source.txt', 'w') as file:
    file.write('テストです')

shutil.copyfile('./data/source.txt', './data/destination.txt')
print('コピーできました')
