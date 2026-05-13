# Cloud Monitoring Script

A Python-based monitoring tool that tracks CPU, memory, and disk usage in real time, outputs structured JSON logs, stores alerts, and integrates with Google Cloud Logging for centralized observability.

The application runs locally, inside Docker, and on a Google Cloud VM as a persistent background service managed by systemd.

---

## Features

- Real-time CPU, memory, and disk monitoring
- Modular Python structure (functions + main loop)
- Structured JSON log output
- Local log persistence (`monitor.log`)
- Alert logging (`alerts.log`)
- Dockerized for portable execution
- Persistent Docker volume support
- Runs as a background service using systemd
- Auto-restart and auto-start on VM boot
- Google Cloud Logging integration
- Centralized log monitoring in GCP Logs Explorer
- IAM-based cloud logging permissions

---

## Architecture

```text
monitor.py
   ↓
Python logging
   ↓
systemd service
   ↓
Google Cloud Ops Agent
   ↓
Google Cloud Logging
```

---

## Tech Stack

- Python
- psutil
- Docker
- Google Cloud Platform (Compute Engine)
- Google Cloud Logging
- Google Cloud Ops Agent
- systemd
- Linux (Ubuntu)

---

## Local Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
python monitor.py
```

---

## Docker Setup

Build image:

```bash
docker build -t monitoring-app .
```

Run container:

```bash
docker run -v $(pwd):/app monitoring-app
```

---

## Google Cloud VM Deployment

### 1. Enable APIs

Enable:
- Compute Engine API
- Cloud Logging API

---

### 2. Create VM

Recommended:
- Ubuntu LTS
- e2-micro machine type

---

### 3. SSH into VM

Install dependencies:

```bash
sudo apt update
sudo apt install python3-pip git -y
```

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/cloud-monitoring-project.git
cd cloud-monitoring-project
```

Install requirements:

```bash
pip3 install -r requirements.txt
```

---

## Google Cloud Logging Integration

The script uses Python logging:

```python
logging.info(json.dumps(data))
```

Logs are collected by the Google Cloud Ops Agent and forwarded to Google Cloud Logging.

---

## IAM Configuration (Important)

The VM service account must have:

```text
Logs Writer
```

Otherwise logs will not appear in Cloud Logging.

Path:

```text
IAM & Admin → IAM → Service Account → Add Role → Logs Writer
```

---

## Run as a systemd Service

Create service file:

```bash
sudo nano /etc/systemd/system/monitor.service
```

Service configuration:

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

Enable and start service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable monitor
sudo systemctl start monitor
```

Check service status:

```bash
sudo systemctl status monitor
```

---

## View Logs

### Local VM logs

```bash
tail -f /var/log/monitor.log
```

### Google Cloud Logs Explorer

Example query:

```text
resource.type="gce_instance"
jsonPayload.message:"cpu"
```

---

## Configuration

```python
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 70
DISK_THRESHOLD = 70
```

---

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

---

## Notes

- Docker metrics reflect container-level resources
- VM deployment reflects real machine resources
- Service continues running independently of SSH session
- Logs can be monitored centrally in Google Cloud
- IAM permissions are required for cloud log delivery

---

## Purpose

This project demonstrates practical DevOps and SRE concepts including:

- Infrastructure monitoring
- Structured logging
- Cloud observability
- Linux service management
- Containerization
- Cloud VM deployment
- IAM troubleshooting
- Centralized log analysis


