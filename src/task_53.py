import os

file_path = '../data/check_file.txt'

if os.path.exists(file_path):
    size = os.path.getsize(file_path)
    if size == 0:
        print("ファイルは空です")
    else:
        print(f"ファイルのサイズは{size}バイトです")
else:
    print("ファイルが見つかりません")