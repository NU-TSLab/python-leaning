# task_54.py
import shutil

with open('./data/source.txt', 'w') as file:
    file.write('Python_task_54')

shutil.copyfile('./data/source.txt', './data/copy.txt')
print('ファイルのコピーが完了しました')
