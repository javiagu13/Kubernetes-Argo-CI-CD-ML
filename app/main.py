import os
import random
import time

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Prometheus
Instrumentator().instrument(app).expose(app)

VERSION = os.getenv("VERSION", "v1")
FAILURE_RATE = float(os.getenv("FAILURE_RATE", "0"))
LATENCY_MS = int(os.getenv("LATENCY_MS", "0"))


class PredictionRequest(BaseModel):
    value: float


@app.get("/")
def root():
    return {
        "service": "inference-api",
        "version": VERSION
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ready")
def ready():
    return {"status": "ready"}


@app.post("/predict")
def predict(request: PredictionRequest):
    # Simulate model inference latency
    if LATENCY_MS > 0:
        time.sleep(LATENCY_MS / 1000)

    # Simulate failures for deployment experiments
    if FAILURE_RATE > 0 and random.random() < FAILURE_RATE:
        raise HTTPException(
            status_code=500,
            detail="Simulated inference failure"
        )

    return {
        "prediction": request.value * 2,
        "version": VERSION
    }
