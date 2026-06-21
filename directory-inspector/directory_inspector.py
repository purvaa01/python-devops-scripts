import os

def inspect_directory(path):

    try:
        if not os.path.exists(path):
            print("Path does not exist")
            return

        if not os.path.isdir(path):
            print("Path exists, but is not a directory")
            return

        files = []
        directories = []
        total_size = 0

        items = os.listdir(path)

        for item in items:

            item_path = os.path.join(path, item)

            if os.path.isfile(item_path):
                files.append(item)
                total_size += os.path.getsize(item_path)

            else:
                directories.append(item)

        print(f"\nDirectory: {path}\n")

        print("Files:")
        for file in files:
            print(file)

        print("\nDirectories:")
        for directory in directories:
            print(directory)

        print("\n--")
        print(f"Total Files: {len(files)}")
        print(f"Total Directories: {len(directories)}")
        print(f"Total Size: {total_size} bytes")

    except Exception as e:
        print(f"Error: {e}")


path = input("Enter directory path: ")
inspect_directory(path)