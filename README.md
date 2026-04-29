# Cloud Monitoring Script

A Python-based monitoring tool that tracks CPU, memory, and disk usage in real time, outputs JSON data, logs metrics, and triggers alerts based on thresholds.

The application runs locally, inside Docker, and on a cloud VM as a background service.

## Features

* Real-time CPU, memory, and disk monitoring
* Modular code structure (functions + main)
* JSON-formatted output
* Logging to `monitor.log`
* Alerts saved in `alerts.log`
* Dockerized for portable execution
* Persistent logs using Docker volume
* Runs as a background service on a VM (systemd)
* Auto-restart and auto-start on boot

## Tech Stack

* Python
* psutil
* Docker
* Google Cloud VM (Compute Engine)
* systemd

## Setup & Run

### Local

```bash
pip install -r requirements.txt
python monitor.py
```

### Docker

```bash
docker build -t monitoring-app .
docker run -v $(pwd):/app monitoring-app
```

### Cloud VM (GCP)

```bash
# SSH into VM
sudo apt update
sudo apt install python3-pip git -y

git clone https://github.com/YOUR_USERNAME/cloud-monitoring-project.git
cd cloud-monitoring-project

pip3 install -r requirements.txt
python3 monitor.py
```

## Run as a Service (systemd)

Create a service file:

```bash
sudo nano /etc/systemd/system/monitor.service
```

```ini
[Unit]
Description=Cloud Monitoring Script
After=network.target

[Service]
User=YOUR_USERNAME
WorkingDirectory=/home/YOUR_USERNAME/cloud-monitoring-project
ExecStart=/usr/bin/python3 monitor.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable monitor
sudo systemctl start monitor
```

Check status:

```bash
sudo systemctl status monitor
```

## Configuration

```python
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 70
DISK_THRESHOLD = 70
```

## Example Output

```json
{
  "timestamp": "2026-04-15 10:45:00",
  "cpu": 12.5,
  "memory": 63.2,
  "disk": 48.1,
  "status": "OK"
}
```

## Notes

* Logs are persisted locally when using Docker volume
* Metrics inside Docker reflect container environment
* On VM, metrics reflect real system resources
* Service runs independently of SSH session

## Purpose

This project demonstrates core DevOps concepts: monitoring, logging, alerting, containerization, cloud deployment, and service management.
