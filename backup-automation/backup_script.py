import os
import shutil

def backup(source_path):
    try:
        if not os.path.exists(source_path):
            print("Path does not exist")
            return

        if not os.path.isdir(source_path):
            print("Not a directory")
            return
        print("It's a directory")

        backup_dir = "backup"

        os.makedirs(backup_dir, exist_ok=True)
        print("Backup directory created\n")

        copied_files = 0
        for item in os.listdir(source_path):
            item_path = os.path.join(source_path, item)

            if os.path.isfile(item_path):
                shutil.copy(item_path, backup_dir)
                print(f"Copied: {item}")
                copied_files += 1

        if copied_files == 0:
            print("No files found to backup")
        else:
            print("backup completed successfully")
            print(f"Files copied: {copied_files}")

    except Exception as e:
        print(f"Error: {e}")

source_path = input("Enter directory path: ")
backup(source_path)