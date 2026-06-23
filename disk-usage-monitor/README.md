# Disk Usage Monitor

A Python script that monitors disk usage on a Linux system and generates a warning when usage exceeds a defined threshold.

## Features

* Checks disk usage using the `df -h` command
* Extracts disk usage percentage
* Monitors filesystem utilization
* Displays system status
* Generates alerts when disk usage exceeds the threshold

## Technologies Used

* Python
* subprocess module
* Linux `df` command

## How to Run

```bash
python3 script.py
```

## Example Output

### Healthy Status

```text
===== DISK USAGE REPORT =====

Disk Usage: 31%

Status: Healthy
```

### Alert Status

```text
===== DISK USAGE REPORT =====

Disk Usage: 91%

WARNING: Disk usage exceeds threshold!
```

## How It Works

The script:

1. Executes the `df -h` command
2. Captures the command output
3. Extracts the disk usage percentage
4. Converts the percentage into an integer
5. Compares the value against a threshold
6. Displays the appropriate status message

## Learning Outcome

This project helped me practice:

* Working with Python's `subprocess` module
* Parsing command output
* String manipulation
* Conditional logic
* Basic monitoring and alerting concepts

**Key takeaway:** Monitoring is not just about collecting data. The real value comes from analyzing that data and taking action when predefined conditions are met.

## Project Structure

```text
disk-usage-monitor/
├── script.py
├── README.md
└── screenshots/
```
