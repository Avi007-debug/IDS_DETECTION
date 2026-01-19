from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.predict import router

app = FastAPI(title="Multi-Stage IDS")

# Global detection storage (circular buffer - keeps last 500)
detections_history = []

# Threat-only storage (keeps last 1000 attacks permanently)
threats_storage = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def health():
    return {"status": "IDS backend running"}

@app.get("/detections")
def get_detections():
    return detections_history

@app.get("/threats")
def get_threats():
    """Returns only detected attacks/threats"""
    return threats_storage

@app.delete("/threats")
def clear_threats():
    """Clear all stored threats"""
    threats_storage.clear()
    return {"status": "threats cleared", "count": 0}

@app.post("/report")
def report_detection(detection: dict):
    # Add to general detections (circular buffer)
    detections_history.append(detection)
    if len(detections_history) > 500:
        detections_history.pop(0)
    
    # If it's an attack, also store in threats (larger limit)
    if detection.get("is_attack", False):
        threats_storage.append(detection)
        if len(threats_storage) > 1000:
            threats_storage.pop(0)
    
    return {"status": "reported"}
