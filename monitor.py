import psutil
import time
from datetime import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 50
DISK_THRESHOLD = 50


def check_alert(value, threshold, name, timestamp):
    if value > threshold:
        alert = f"⚠️ HIGH {name} ALERT: {value}%"
        print(alert)

        with open("alerts.log", "a") as f:
            f.write(f"{timestamp} | {alert}\n")


while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = f"{timestamp} | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"
    print(log)

    # Run alert checks
    check_alert(cpu, CPU_THRESHOLD, "CPU", timestamp)
    check_alert(memory, MEMORY_THRESHOLD, "MEMORY", timestamp)
    check_alert(disk, DISK_THRESHOLD, "DISK", timestamp)

    # Save monitoring log
    with open("monitor.log", "a") as file:
        file.write(log + "\n")

    time.sleep(2)


  
