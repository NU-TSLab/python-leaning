import os

file_path = './data/check_file.txt'
if os.path.exists(file_path):
    file_size = os.path.getsize(file_path)
    if file_size == 0:
        print('�t�@�C���͋�ł�')
    else:
        print(f'�t�@�C���̃T�C�Y�� {file_size} �o�C�g�ł�')
else:
    print('�t�@�C�������݂��܂���')