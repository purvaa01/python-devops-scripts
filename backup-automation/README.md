# Backup Automation Script

A Python script that automates file backups by copying all files from a source directory into a backup folder.

## Features

* Validates whether a directory exists
* Verifies the provided path is a directory
* Creates a backup directory automatically
* Copies all files from the source directory
* Counts the number of files backed up
* Handles errors gracefully

## Technologies Used

* Python
* os module
* shutil module

## How to Run

```bash
python3 backup_script.py
```

Enter the source directory path when prompted.

## Example Output

### Successful Backup

```text
Enter directory path: /mnt/d/Projects

It's a directory
Backup directory created

Copied: abc.txt

Backup completed successfully
Files copied: 1
```

### Invalid Path

```text
Enter directory path: /mnt/d/InvalidDirectory

Path does not exist
```

### Not a Directory

```text
Enter directory path: abc.txt

Not a directory
```

## Learning Outcome

This project helped me practice:

* Directory validation
* File operations
* Working with the `os` module
* Using the `shutil` module for file backups
* Loops and conditional logic
* Exception handling

**Key takeaway:** Before performing backup operations, scripts should validate paths and handle failures gracefully to avoid unexpected behavior.

## Project Structure

```text
backup-automation/
├── backup_script.py
├── README.md
└── screenshots/
```
