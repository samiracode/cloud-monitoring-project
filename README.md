# Cloud Monitoring & Alerting System

A Python-based cloud monitoring application that tracks CPU, memory, and disk usage in real time, generates structured logs, stores alerts, and integrates with Google Cloud Logging, Monitoring, and Alerting for centralized observability.

The application runs:
- locally
- inside Docker
- on a Google Cloud VM as a persistent Linux service using systemd

This project demonstrates practical DevOps, Cloud Engineering, and SRE concepts including monitoring, logging, alerting, cloud deployment, IAM troubleshooting, and dashboard visualization.

---

# Features

- Real-time CPU, memory, and disk monitoring
- Structured JSON log generation
- Local log persistence (`monitor.log`)
- Alert logging (`alerts.log`)
- Multi-alert support (`HIGH CPU`, `HIGH MEMORY`, `HIGH DISK`)
- Dockerized application
- Persistent Docker volume support
- Linux background service using systemd
- Auto-restart and auto-start on boot
- Google Cloud Logging integration
- Google Cloud Monitoring dashboards
- Log-based metrics
- Email alerting policies
- IAM-based logging permissions
- Centralized observability in Google Cloud

---

# Architecture

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
    ↓
Log-based Metrics
    ↓
Alert Policies
    ↓
Email Notifications + Dashboards