import subprocess

def get_disk_usage():
    result = subprocess.run(
        "df -h",
        shell=True,
        capture_output=True,
        text=True
    )
    print(result.stdout)

def get_memory_usage():
    result = subprocess.run(
        "free -h",
        shell=True,
        capture_output=True,
        text=True
    )
    print(result.stdout)

def get_uptime():
    result = subprocess.run(
        "uptime",
        shell=True,
        capture_output=True,
        text=True
    )
    print(result.stdout)

print("--system health report--")
print("-----")
print("Disk usage:")
get_disk_usage()
print("-----")
print("Memory Usage:")
get_memory_usage()
print("-----")
print("System Uptime:")
get_uptime()
