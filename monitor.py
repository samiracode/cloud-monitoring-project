import psutil
import time
from datetime import datetime

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = f"{timestamp} | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"

    print(log)

    with open("monitor.log", "a") as file:
        file.write(log + "\n")

    time.sleep(2)