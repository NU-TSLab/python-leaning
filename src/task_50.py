import os
current_directory=os.getcwd()
print(f"Current_derectory:{current_directory}")
directory_contents=os.listdir(current_directory)
print(f"Directory contents:{directory_contents}")