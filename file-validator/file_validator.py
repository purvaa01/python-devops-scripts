import os

def validate_file(file_path):
    try:
        if not os.path.exists(file_path):
            print("File does not exists")
            return

        if not os.path.isfile(file_path):
            print("Path exists but is not a file")
            return

        print("file validation successful")
        print(f"File Name: {os.path.basename(file_path)}")
        print(f"size: {os.path.getsize(file_path)} bytes")
        print(f"Absolute Path: {os.path.abspath(file_path)}")

    except Exception as e:
        print(f"Enter :{e}")

path = input("enter file path: ")
validate_file(path)



