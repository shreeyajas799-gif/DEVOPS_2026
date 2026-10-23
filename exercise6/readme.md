# Exercise 6: Real-Time Operations Monitoring and Alerting

## Objective
Monitor ZAPPTTO delivery operations using Python, Prometheus, Grafana, Docker, and Jenkins.

## Technologies
- Python
- Prometheus
- Grafana
- Docker & Docker Compose
- Jenkins

## Features
- Simulates delivery metrics such as total, pending, and on-the-way deliveries.
- Exposes metrics through a Prometheus `/metrics` endpoint.
- Visualizes delivery performance using Grafana dashboards.
- Configures alerts for high pending deliveries and delivery times.
- Supports automated deployment through Jenkins pipelines.

## Run the Application
```bash
docker compose up -d --build
```

## Access Services
- Metrics: http://localhost:8000/metrics
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3001

## Expected Outcome
A monitoring dashboard displaying delivery metrics and Prometheus alerts for potential operational issues.
