import os

if os.path.exists('./data/check_file.txt'):
    file_size = os.path.getsize('./data/check_file.txt')
    if file_size == 0:
        print('ファイルサイズはゼロ')
    else:
        print(f'ファイルサイズ：{file_size}')

else:
    print('ファイルが存在しない')