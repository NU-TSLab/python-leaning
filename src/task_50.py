import os

current_directory = os.getcwd()
print(f"Current directory:{current_directory}")

directory_contents = os.listdir(current_directory)
print(f"Current directory:{directory_contents}")