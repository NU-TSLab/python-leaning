import os

file_path = './data/check_file.txt'
if os.path.exists(file_path):
    file_size = os.path.getsize(file_path)
    if file_size == 0:
        print(f"File '{file_path}' is empty.")
    else:
        print(f"File '{file_path}': {file_size} bytes.")
else:
    print(f"File '{file_path}' does not exist.")

#g/src/task_53.py
#File './data/check_file.txt': 2927 bytes.