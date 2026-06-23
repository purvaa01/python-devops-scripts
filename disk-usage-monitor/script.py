import subprocess

def get_disk_usage():
    result = subprocess.run(
        "df -h",
        shell=True,
        capture_output=True,
        text=True
    )

    output = result.stdout
    lines = output.splitlines()
    disk_info = lines[3].split()
    usage = disk_info[4]
    usage = usage.replace("%", "")
    usage = int(usage)
    print(usage)
    if usage > 80:
        print("WARNING: Disk usage exceed threshold")
    else:
        print("STATUS: Healthy")

print("Disk Usage:")
get_disk_usage()