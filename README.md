# Cloud Monitoring Script

A simple Python tool that monitors CPU, memory, and disk usage in real time, logs system metrics, and outputs structured JSON data. It also triggers alerts when system thresholds are exceeded.

## Features

* Real-time CPU, memory, and disk monitoring
* Modular code structure (functions + main entry point)
* JSON-formatted output (machine-friendly)
* Logs data to `monitor.log`
* Alerts on high resource usage (`alerts.log`)
* Continuous monitoring loop

## Tech Stack

* Python
* psutil

## Setup & Run

```bash
pip install -r requirements.txt
python monitor.py
```

## Configuration

You can adjust thresholds in `monitor.py`:

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

* Log files are created automatically
* Logs are ignored by `.gitignore`
* Alerts are triggered only when thresholds are exceeded

## Purpose

This project demonstrates foundational Cloud/DevOps concepts such as monitoring, logging, alerting, and structured data output.
