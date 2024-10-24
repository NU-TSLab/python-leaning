import shutil

with open('./data/source.txt', 'w') as file:
    file.write('This is a source file.')

shutil.copyfile('./data/source.txt', './data/destination.txt')
print('ファイルのコピーが完了しました')