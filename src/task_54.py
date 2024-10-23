import shutil

# ファイルの作成と書き込み
with open('./data/source.txt', 'w') as file:
    file.write('This is a source file.')

# ファイルのコピー
shutil.copyfile('./data/source.txt', './data/destination.txt')
print('ファイルのコピーが完了しました')