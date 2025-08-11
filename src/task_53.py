import os

if os.path.isfile("data/check_file.txt"):
    size = os.stat("data/check_file.txt").st_size
    print(f'ファイルサイズ: {size}バイト')
else:
    print('ファイルが存在しません')