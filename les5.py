import os
import shutil
# 1. יצירת תיקייה חדשה

directory_name = "l5"

try:
    os.mkdir(directory_name)
    print(f"Directory '{directory_name}' created successfully.")
except FileExistsError:
    print(f"Directory '{directory_name}' already exists.")
except PermissionError:
    print(f"Directory '{directory_name}' is not readable.")
except Exception as e:
    print(f"An error occurred: {e}")

# 3,4. יצירת קובץ בתוך התיקייה + כתיבה בו

file_path = os.path.join(directory_name, 'new_file.txt')

try:
    with open(file_path, 'w') as file:
        file.write("Hello, world!")
    print(f"File '{file_path}' created successfully.")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")

# 5. מחיקת קובץ
try:
    os.remove(file_path)
    print(f"File '{file_path}' has been removed successfully.")
except FileNotFoundError:
    print(f"File '{file_path}' does not exist.")
except PermissionError:
    print(f"Permission denied: Cannot delete the file '{file_path}'.")
except Exception as e:
    print(f"An error occurred while removing the file: {e}")

# 2.מחיקת תיקיה
location = r'E:\זהבי\תכנות\יד\Pyton\ש.ב\5'
path = os.path.join(location, directory_name)

try:
    shutil.rmtree(path)
    print(f"Directory '{path}' has been removed successfully.")
except FileNotFoundError:
    print(f"Directory '{path}' does not exist.")
except OSError as e:
    print(f"Error: {e}")

current_path = os.getcwd()

print(f"Current folder path: {current_path}")
