import psutil
import time
import json
from datetime import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 70
DISK_THRESHOLD = 70


# --- Metric Functions ---
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    return psutil.virtual_memory().percent


def get_disk_usage():
    return psutil.disk_usage('/').percent


# --- Status Check ---
def check_status(cpu, memory, disk):
    if cpu > CPU_THRESHOLD:
        return "HIGH CPU"
    if memory > MEMORY_THRESHOLD:
        return "HIGH MEMORY"
    if disk > DISK_THRESHOLD:
        return "HIGH DISK"
    return "OK"


# --- Main Function ---
def main():
    while True:
        cpu = get_cpu_usage()
        memory = get_memory_usage()
        disk = get_disk_usage()

        status = check_status(cpu, memory, disk)

        data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "cpu": cpu,
            "memory": memory,
            "disk": disk,
            "status": status
        }

        # Print JSON output
        print(json.dumps(data, indent=2))

        # Save logs
        with open("monitor.log", "a") as f:
            f.write(json.dumps(data) + "\n")

        # Save alerts
        if status != "OK":
            with open("alerts.log", "a") as f:
                f.write(json.dumps(data) + "\n")

        time.sleep(2)


# --- Entry Point ---
if __name__ == "__main__":
    main()


  
