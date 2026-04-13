import psutil
import time
from datetime import datetime

CPU_THRESHOLD = 80

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = f"{timestamp} | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"

    print(log)

    # ALERT condition
    if cpu > CPU_THRESHOLD:
        alert = f"⚠️ HIGH CPU ALERT: {cpu}%"
        print(alert)

        with open("alerts.log", "a") as f:
            f.write(f"{timestamp} | {alert}\n")

    with open("monitor.log", "a") as file:
        file.write(log + "\n")

    time.sleep(2)