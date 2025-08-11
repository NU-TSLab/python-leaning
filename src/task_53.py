import os

if os.path.exists('./data/check_file.txt'):
    file_size=os.path.getsize('./data/check_file.txt')
    if file_size==0:
        print("ファイルは空です")
    else:
        print(f"ファイルのサイズは{file_size}バイトです")
else:
    print("ファイルが存在しません")