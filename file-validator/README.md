# File Validator

A simple Python script that validates file paths before execution.

## Features

* Checks if a file exists
* Verifies that the path is a file
* Displays file name and size
* Shows the absolute file path
* Handles errors gracefully

## Technologies Used

* Python
* os module

## How to Run

```bash
python3 file_validator.py
```

Enter a file path when prompted.

## Example Output

### Successful Validation

![Validation Successful](screenshots/validation-success.png)

```text
enter file path: /path/to/file.txt

File validation successful
File Name: file.txt
Size: 484 bytes
Absolute Path: /path/to/file.txt
```

### Validation Failure

![Validation Failed](screenshots/validation-fail.png)

```text
enter file path: file.txt

File does not exist
```

## Learning Outcome

This project helped me practice:

* File handling
* Input validation
* Exception handling
* Working with the `os` module

**Key takeaway:** Reliable automation starts with validation before execution.

## Project Structure

```text
file-validator/
├── file_validator.py
├── README.md
└── screenshots/
```
