# Directory Inspector

A Python script that inspects a directory and provides a summary of its contents.

## Features

* Validates whether a directory exists
* Verifies the provided path is a directory
* Lists all files
* Lists all subdirectories
* Counts files and directories
* Calculates total file size
* Handles errors gracefully

## Technologies Used

* Python
* os module

## How to Run

```bash
python3 directory_inspector.py
```

Enter a directory path when prompted.

## Example Output

### Successful Inspection

```text
Enter directory path: /home/purva/project

Directory: /home/purva/project

Files:
app.py
README.md
requirements.txt

Directories:
logs
templates
static

--------------------
Total Files: 3
Total Directories: 3
Total Size: 8421 bytes
```

### Invalid Path

```text
Enter directory path: /home/purva/test

Path does not exist
```

### Not a Directory

```text
Enter directory path: app.py

Path exists, but is not a directory
```

## Learning Outcome

This project helped me practice:

* Directory handling
* File inspection
* Path validation
* Working with the `os` module
* Loops and conditional logic
* Exception handling

**Key takeaway:** Before automating operations on a directory, validate the path and understand its contents.

## Project Structure

```text
directory-inspector/
├── directory_inspector.py
├── README.md
└── screenshots/
```
