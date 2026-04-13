# Cloud Monitoring Script

A simple Python tool that monitors CPU, memory, and disk usage in real time, logs system metrics, and triggers alerts when CPU usage is high.

## Features

* Real-time system monitoring
* Logs data to `monitor.log`
* Alerts on high CPU usage (`alerts.log`)
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

You can change the CPU alert threshold in `monitor.py`:

```python
CPU_THRESHOLD = 80
```

## Notes

* Log files are created automatically
* Logs are ignored by `.gitignore`

## Purpose

This project demonstrates basic monitoring, logging, and alerting concepts used in Cloud/DevOps environments.


