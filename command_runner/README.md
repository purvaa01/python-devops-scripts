# Linux Command Runner

A Python script that executes Linux commands and displays their output. This project demonstrates how Python can interact with the operating system using the `subprocess` module.

## Features

* Accepts Linux commands as user input
* Executes commands using Python
* Displays command output
* Handles invalid commands gracefully
* Captures both standard output and errors

## Technologies Used

* Python
* subprocess module

## How to Run

```bash
python3 script.py
```

Enter a Linux command when prompted.

## Example Output

### Successful Command

```text
Enter the command you want to run:
pwd

Output:
/mnt/d/Projects/Python-devops-scripts/command_runner
```

### Another Successful Command

```text
Enter the command you want to run:
whoami

Output:
purvaa
```

### Invalid Command

```text
Enter the command you want to run:
abcd

Command Failed:
/bin/sh: 1: abcd: not found
```

## Learning Outcome

This project helped me practice:

* Working with the `subprocess` module
* Executing Linux commands from Python
* Capturing command output
* Handling command failures
* Error handling and validation

**Key takeaway:** Automation becomes much more powerful when scripts can interact directly with the operating system and respond to command results.

## Project Structure

```text
command-runner/
├── script.py
├── README.md
└── screenshots/
```
