import shutil

# ファイルの作成と書き込み
with open('C:\\Users\\csfu2\\Documents\\Python_git_study\\python-leaning\\data\\source.txt', 'w') as file:
    file.write('This is a source file.')

# ファイルのコピー
shutil.copyfile('C:\\Users\\csfu2\\Documents\\Python_git_study\\python-leaning\\data\\source.txt', 'C:\\Users\\csfu2\\Documents\\Python_git_study\\python-leaning\\data\\destination.txt')
print('ファイルのコピーが完了しました')