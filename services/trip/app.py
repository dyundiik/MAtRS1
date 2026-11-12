import os
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title=os.getenv("SERVICE_NAME", "tripack-service"))
Instrumentator().instrument(app).expose(app)

@app.get("/health")
def health():
    return {"status": "ok", "service": os.getenv("SERVICE_NAME", "tripack-service")}

@app.get("/")
def root():
    return {"service": os.getenv("SERVICE_NAME", "tripack-service"),
            "message": "TripPack service scaffold; business endpoints are planned for the next practical work."}
