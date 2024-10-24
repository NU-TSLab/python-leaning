import os
if os.path.exists("./data/check_file.txt"):
    n = os.path.getsize("./data/check_file.txt")
    if(n == 0):
        print("ファイルは空ですよ。")
    else:
        print("ファイルのサイズは",n,"バイトです。")
else:
    print("ファイル無し。")