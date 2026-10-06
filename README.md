# Production Deployment Demo

A small CPU-only FastAPI service for learning production deployment concepts:

- Docker
- Kubernetes
- Helm
- Rolling deployments
- Blue/green deployments
- Canary releases
- A/B routing
- Prometheus/Grafana
- Argo CD
- Argo Rollouts
- Automated rollback

## Current step

The first step is a minimal inference-like API.

### Run locally

```bash
cd app
pip install -r requirements.txt
uvicorn main:app --reload
```

Test:

```bash
curl http://localhost:8000/
```

```bash
curl -X POST http://localhost:8000/predict   -H "Content-Type: application/json"   -d '{"value": 10}'
```

## Environment variables

`VERSION` controls the service version:

```bash
VERSION=v2
```

`LATENCY_MS` simulates inference latency:

```bash
LATENCY_MS=200
```

`FAILURE_RATE` simulates failures:

```bash
FAILURE_RATE=0.2
```

Example:

```bash
VERSION=v2 LATENCY_MS=200 FAILURE_RATE=0.1 uvicorn main:app --port 8001
```

The same application will later be deployed as multiple Kubernetes versions so we can practice rolling, blue/green, canary, A/B, monitoring, and rollback strategies.
