import subprocess

def run_command(command):
    res = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    if res.returncode == 0:
        print(f"output:\n{res.stdout}")
    else:
        print(f"command failed:\n{res.stderr}")

command = input("enter the command u want to run:\n")
run_command(command)