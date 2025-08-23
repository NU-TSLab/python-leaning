import os

file='./data/check_file.txt'
if os.path.isfile(file):
    size=os.stat(file).st_size
    if size==0:
        print("ファイルは空です。")
    else:
        print(f"ファイルのサイズは{size}バイトです。")
else:
    print("ファイルは存在しません。")
