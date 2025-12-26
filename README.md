# 🚨 Multi-Stage Intrusion Detection System (IDS)

A real-time **Machine Learning–based Intrusion Detection System** that detects network attacks using
**flow-level analysis**, **multi-stage ML models**, and **live packet capture with Scapy**.

This project demonstrates a **production-style IDS architecture**, not a toy classifier.

---

## 📌 Key Features

- 🔍 **Multi-Stage Detection Pipeline**
  - Stage 1: Normal traffic confidence filter
  - Stage 2: Specialized attack classifiers (DoS, DDoS, PortScan, BruteForce, WebAttack)
- 📡 **Real-Time Packet Capture** using Scapy
- 📊 **Flow-Based Feature Extraction** (CICIDS-style)
- 🧠 **ML Models trained on CICIDS-2017 dataset**
- ⚙️ **Feature-order safe inference**
- 🚫 Prevents Normal-class dominance
- 🔁 Thread-safe, clean shutdown IDS sensor
- 🌐 REST API support using FastAPI

---

## 🏗️ Architecture Overview

Packets (Scapy)
↓
Flow Aggregation (5-tuple)
↓
Feature Extraction
↓
Stage 1: Normal Filter (ML)
↓
Stage 2: Attack Models (One-vs-Rest)
↓
Final Decision (Highest confidence / Unknown)

yaml
Copy code

---

## 🧠 Detection Logic

### Stage 1 — Normal Filter
- Predicts probability of **BENIGN**
- If `P(Normal) ≥ 0.9` → classified as Normal
- Else → forwarded to attack classifiers

### Stage 2 — Attack Models
Each model is trained independently on the **same feature space**:
- DoS
- DDoS
- PortScan
- BruteForce (FTP / SSH)
- WebAttack

If no attack exceeds threshold → **Unknown Attack**

---

## 📂 Project Structure

IDS_02/
│
├── backend/
│ ├── app/
│ │ ├── api/ # FastAPI endpoints
│ │ ├── realtime/ # Scapy sniffing & flow logic
│ │ ├── decision.py # Final IDS decision logic
│ │ ├── feature_mapper.py # Payload → feature vector
│ │ └── models_loader.py # Load ML models safely
│ │
│ ├── models/ # Trained ML models (.pkl)
│ ├── artifacts/ # Feature order, metadata
│ └── requirements.txt
│
└── README.md

yaml
Copy code

---

## 🚀 How to Run (Backend)

### 1️⃣ Install dependencies
```bash
cd backend
pip install -r requirements.txt
2️⃣ Start FastAPI server
bash
Copy code
uvicorn app.main:app --reload
3️⃣ Start IDS sensor (Scapy)
⚠️ Run terminal as Administrator

bash
Copy code
python -c "from app.realtime.sniffer import start_sniffing; start_sniffing()"
🧪 Live Testing
Generate traffic in another terminal:

bash
Copy code
ping -t 8.8.8.8
Detected flows will be printed as:

yaml
Copy code
=== FLOW DETECTED ===
Flow: (...)
IDS Result: {...}
📊 Dataset Used
CICIDS-2017 (flow-based network intrusion dataset)

## Multi-Stage Intrusion Detection System (IDS)

A production-oriented Intrusion Detection System that performs flow-level feature extraction from live traffic and runs a multi-stage machine-learning inference pipeline to detect attacks (DoS, DDoS, PortScan, BruteForce, WebAttack, etc.).

This repository contains the backend server (FastAPI) and the realtime sensor (Scapy-based) used for flow aggregation and inference.

## Highlights

- Multi-stage detection pipeline (Normal filter → per-attack classifiers)
- Flow-level feature extraction (CICIDS-style features)
- Live packet capture using Scapy
- FastAPI backend with a prediction endpoint
- Models are loaded at runtime for inference (trained offline)

## Quick links

- Backend app entry: `backend/app/main.py`
- Realtime sensor: `backend/app/realtime/sniffer.py`
- Prediction endpoint: `backend/app/api/predict.py`
- Requirements: `backend/requirements.txt`

## Prerequisites

- Python 3.8+ installed
- On Windows: run the realtime sensor with Administrator privileges (required for packet capture)

Recommended: create a virtual environment before installing dependencies.

## Setup (Windows PowerShell)

Open PowerShell (preferably as Administrator if you plan to run the realtime sniffer):

```powershell
# create and activate a virtual environment
cd C:\Users\Giri Vardhan\IDS_02\backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

Notes:
- If Execution Policy blocks activation, run PowerShell as Administrator and enable scripts for the current session:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

## Running the backend API

Start the FastAPI server (development mode):

```powershell
# from backend directory (virtualenv activated)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Health check: open http://127.0.0.1:8000/ and you should see JSON like `{ "status": "IDS backend running" }`.

Prediction endpoint: see `backend/app/api/predict.py` for the REST route and payload format.

## Running the realtime IDS sensor (Scapy)

Important: packet capture requires elevated privileges. Run PowerShell as Administrator.

From `backend` (with virtualenv activated):

```powershell
# Run the sniffer (starts Scapy sniff + flow monitor)
python -c "from app.realtime.sniffer import start_sniffing; start_sniffing()"
```

The sensor will print detected flows and inference results to the console:

```
=== FLOW DETECTED ===
Flow: (<5-tuple>)
Features: {...}
IDS Result: {...}
```

### Tips for testing

- Generate benign traffic using `ping 8.8.8.8 -t` (Windows) in a separate terminal.
- Use PCAPs or controlled packet generators to simulate attacks when testing the detection models.

## Project layout

```
IDS_02/
├── backend/
│   ├── app/
│   │   ├── api/                # FastAPI endpoints (predict/realtime)
│   │   ├── realtime/           # sniffer, flow table, feature extractor
│   │   ├── decision.py         # multi-stage decision logic
│   │   ├── feature_mapper.py   # feature alignment and ordering
│   │   └── models_loader.py    # loads ML models and metadata
│   ├── artifacts/              # feature-order, encoder metadata
│   ├── models/                 # serialized ML models (.pkl / joblib)
│   └── requirements.txt
├── README.md
```

## Models and artifacts

- Models are expected under `backend/models/` and metadata (feature order, encoders) under `backend/artifacts/`.
- Models are trained offline and are not included in this repo. When adding models, ensure the feature order matches `artifacts/feature_order.json` (or equivalent) used by `feature_mapper.py` and `models_loader.py`.

## Development notes

- The repo separates feature extraction, model loading, and detection logic so models can be retrained and swapped without changing the runtime code.
- Use the FastAPI endpoint for batch/single predictions and the realtime sensor for live flow-based detection.

## Troubleshooting

- If Scapy fails to capture packets on Windows, ensure WindPcap/Npcap is installed and running and that PowerShell is running with Administrator rights.
- For dependency errors, verify that the virtual environment is activated and that `pip install -r requirements.txt` completed successfully.

## Contributing

Contributions are welcome. Please open an issue to discuss larger changes before submitting a PR. Prefer small, focused commits and include tests or instructions to validate behavior.

## License & Author

Author: EGV Santhosh Kumar

Repository: https://github.com/egvsanthoshkumarcy24-glitch

License: (add license file / details here)
