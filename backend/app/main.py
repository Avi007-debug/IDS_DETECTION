from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.predict import router

app = FastAPI(title="Multi-Stage IDS")

# Global detection storage
detections_history = []

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

@app.post("/report")
def report_detection(detection: dict):
    detections_history.append(detection)
    if len(detections_history) > 500:
        detections_history.pop(0)
    return {"status": "reported"}
