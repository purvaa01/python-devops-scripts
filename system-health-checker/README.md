# System Health Checker

A Python script that collects and displays basic Linux system health information by executing system commands through the `subprocess` module.

## Features

* Checks disk usage
* Checks memory usage
* Displays system uptime
* Generates a simple health report
* Handles command execution through Python

## Technologies Used

* Python
* subprocess module
* Linux commands (`df`, `free`, `uptime`)

## How to Run

```bash
python3 script.py
```

## Example Output

```text
--- SYSTEM HEALTH REPORT ---

Disk Usage:
Filesystem      Size  Used Avail Use%
...

Memory Usage:
total        used        free
...

System Uptime:
up 3 hours, 24 minutes

```

## Commands Used

| Command   | Purpose                                  |
| --------- | ---------------------------------------- |
| `df -h`   | Displays disk usage information          |
| `free -h` | Displays memory usage information        |
| `uptime`  | Displays system uptime and load averages |

## Learning Outcome

This project helped me practice:

* Working with Python's `subprocess` module
* Executing Linux commands from Python
* Capturing command output
* Building simple monitoring utilities
* Structuring scripts using functions

**Key takeaway:** Python can act as a bridge between automation logic and operating system commands, making it a powerful tool for system monitoring and DevOps automation.

## Project Structure

```text
system-health-checker/
├── script.py
├── README.md
└── screenshots/
```
