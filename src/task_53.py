import os

file_name = './data/check_file.txt'
if os.path.exists(file_name):
    size = os.path.getsize(file_name)
    if size == 0:
        print(f"ファイルは空です")
    else:
        print(f"ファイルのサイズは{size}バイトです")
else:
    print(f"ファイルが存在しません")