
# Cloud Monitoring Script

A Python-based monitoring tool that tracks CPU, memory, and disk usage in real time, outputs JSON data, logs metrics, and triggers alerts based on thresholds. The app is containerized using Docker.

## Features

* Real-time CPU, memory, and disk monitoring
* Modular code structure (functions + main)
* JSON-formatted output
* Logging to `monitor.log`
* Alerts saved in `alerts.log`
* Dockerized for portable execution
* Persistent logs using Docker volume

## Tech Stack

* Python
* psutil
* Docker

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
* Alerts trigger only when thresholds are exceeded

## Purpose

This project demonstrates core DevOps concepts: monitoring, logging, alerting, containerization, and portability.





