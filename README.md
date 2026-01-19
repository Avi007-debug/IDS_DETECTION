# 🚨 Multi-Stage Intrusion Detection System

Real-time ML-based Intrusion Detection System with flow-level analysis, multi-stage detection pipeline, and live packet capture.

## Features

- **Multi-Stage Detection**: Normal filter → specialized attack classifiers (DoS, DDoS, PortScan, BruteForce, WebAttack)
- **Real-Time Monitoring**: Live packet capture using Scapy with flow-based feature extraction
- **ML Models**: Trained on CICIDS-2017 dataset with 95%+ accuracy
- **Web Dashboard**: React frontend for real-time visualization and alerts
- **REST API**: FastAPI backend with prediction endpoints

## Architecture

```
Packets → Flow Aggregation → Feature Extraction → Stage 1 (Normal Filter) → Stage 2 (Attack Models) → Final Decision
```

## Quick Start

See [SETUP.md](SETUP.md) for detailed installation instructions.

```powershell
# Backend
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

## Project Structure

```
IDS_DETECTION/
├── backend/
│   ├── app/              # FastAPI application
│   ├── models/           # Trained ML models
│   ├── artifacts/        # Feature metadata
│   └── requirements.txt
├── frontend/             # React dashboard
└── IDS_final.ipynb      # Model training notebook
```

## Detection Types

- **DoS/DDoS**: Denial of Service attacks
- **PortScan**: Network reconnaissance
- **BruteForce**: Login credential attacks
- **WebAttack**: SQL injection, XSS, etc.

## Demo

Use the built-in demo scripts to simulate attacks:

```powershell
python backend/demo_attack.py 127.0.0.1 dos
python backend/demo_attack.py 127.0.0.1 portscan
```

See [backend/DEMO_GUIDE.md](backend/DEMO_GUIDE.md) for full presentation guide.

## Requirements

- Python 3.8+
- Node.js 16+
- Administrator privileges (for packet capture)
- Npcap/WinPcap (Windows)

## Author

Avi007-debug

## License

MIT License
