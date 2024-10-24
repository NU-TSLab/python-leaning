import os
file_path = './data/check_file.txt'
if os.path.exists(file_path):
    file_size = os.path.getsize(file_path)
    if file_size == 0:
        print('ファイルは空です')
    else:
        print(f'ファイルサイズは{file_size}バイトです')
else:
    print('ファイルが存在しません')
