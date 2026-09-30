# Practical 8: Monitoring with Prometheus & Grafana (Windows)

## Aim
Monitor a Flask application using Prometheus + Grafana + Windows Exporter.

## Software & Ports

| Software | Purpose | Port |
|----------|---------|------|
| Flask App | Application | 5000 |
| Prometheus Client | App metrics | 8000 |
| Prometheus | Collect metrics | 9090 |
| Windows Exporter | CPU/Memory | 9182 |
| Grafana | Dashboards | 3000 |

---

## Part A — Set up Prometheus

### 1. Download Prometheus for Windows
https://prometheus.io/download/  
Download `prometheus-*.windows-amd64.zip` and extract to `C:\prometheus`

### 2. Configure `prometheus.yml`
Replace contents with:
```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "python-app"
    static_configs:
      - targets: ["localhost:8000"]

  - job_name: "windows"
    static_configs:
      - targets: ["localhost:9182"]
```

---

## Part B — Create Flask Application with Metrics

### 1. Create project
```bash
mkdir C:\monitoring-app
cd C:\monitoring-app
python -m venv venv
venv\Scripts\activate
pip install flask prometheus-client
```

### 2. Create `app.py`
```python
from flask import Flask
from prometheus_client import Counter, start_http_server

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total number of API requests"
)

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Hello! Flask application is running."

@app.route("/hello")
def hello():
    REQUEST_COUNT.inc()
    return "Hello from the monitoring application!"

if __name__ == "__main__":
    start_http_server(8000)   # Prometheus metrics
    app.run(host="0.0.0.0", port=5000)
```

### 3. Run the app
```bash
python app.py
```

Test:
- http://localhost:5000
- http://localhost:8000  (look for `api_requests_total`)

---

## Part C — Start Prometheus
Open **new** CMD:
```bash
cd C:\prometheus
prometheus.exe --config.file=prometheus.yml
```

Open: http://localhost:9090  
Go to Status → Targets → all should be UP.

---

## Part D — Windows Exporter
Download and install **windows_exporter** from GitHub releases.  
It runs as a Windows service on port **9182**.

Verify: http://localhost:9182/metrics

---

## Part E — Grafana

### 1. Install Grafana for Windows
Download from https://grafana.com/grafana/download  
Install and start the service.

### 2. Open Grafana
http://localhost:3000  
Default login: `admin` / `admin`

### 3. Add Prometheus Data Source
- Configuration → Data Sources → Add Prometheus
- URL: `http://localhost:9090`
- Save & Test

### 4. Create Dashboard

**Panel 1 – API Request Rate**
```promql
rate(api_requests_total[1m])
```
Visualization: Time series  
Title: API Request Rate

**Panel 2 – CPU Usage %**
```promql
100 - (100 * avg by (instance) (rate(windows_cpu_time_total{mode="idle"}[5m])))
```
Visualization: Gauge  
Title: CPU Usage %

**Panel 3 – Memory Usage %**
```promql
100 * (1 - windows_memory_available_bytes / windows_memory_physical_total_bytes)
```
Visualization: Gauge  
Title: Memory Usage %

> Metric names can vary. Check exact names at http://localhost:9182/metrics

### 5. Generate traffic
Refresh http://localhost:5000 several times or:
```bash
curl http://localhost:5000/
```

---

## Running Everything (4 processes)

| Process | Command |
|---------|---------|
| Flask | `python app.py` |
| Prometheus | `prometheus.exe --config.file=prometheus.yml` |
| Windows Exporter | Runs as service |
| Grafana | Runs as service |

---

## Architecture
```
Flask App (:5000)
      │ metrics
      ▼
Prometheus Client (:8000)
      │
      ▼
   Prometheus (:9090)  ◄── Windows Exporter (:9182)
      │
      ▼
   Grafana (:3000)
```
