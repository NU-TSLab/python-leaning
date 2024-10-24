import os
os.path.exists("./data/check_file.txt")

size=os.stat("./data/check_file.txt").st_size
if size==0:
    print (f"ファイルは空です")
else:
     print (f"ファイルのサイズは{size}です。")