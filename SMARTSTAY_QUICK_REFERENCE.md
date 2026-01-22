# 🚀 SmartStay IDS Demo - Quick Reference

**Last Updated**: January 2026

---

## Prerequisites

✅ **Required Services Running:**

| Service | URL | Status Check |
|---------|-----|--------------|
| SmartStay Backend | http://127.0.0.1:5000 | Visit URL, see Flask response |
| SmartStay Frontend | http://localhost:8080 | Open in browser |
| IDS Backend | http://127.0.0.1:8000 | Visit URL, see `{"status": "IDS backend running"}` |
| IDS Frontend | http://localhost:5173 | Open in browser |

---

## Quick Start Commands

### 1. Start SmartStay Backend
```powershell
cd C:\Coding\SmartStay\backend
.\venv\Scripts\Activate.ps1
python app.py
```

### 2. Start SmartStay Frontend
```powershell
cd C:\Coding\SmartStay\frontend
npm run dev
```

### 3. Start IDS Backend
```powershell
cd C:\Coding\IDS_DETECTION\backend
.\.venv\Scripts\Activate.ps1
$env:IDS_API_TOKEN = "your-secure-token-here-change-in-production"
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### 4. Start IDS Frontend
```powershell
cd C:\Coding\IDS_DETECTION\frontend
npm run dev
```

### 5. (Optional) Start SmartStay Network Monitor
```powershell
# Quick launcher (as Administrator)
cd C:\Coding\IDS_DETECTION\backend
.\monitor_smartstay.ps1

# OR manual command
.\.venv\Scripts\Activate.ps1
python -c "from app.realtime.sniffer_smartstay import start_sniffing_smartstay; start_sniffing_smartstay()"
```

---

## Running Attacks

### Option 1: Automated Demo Script (Recommended)

```powershell
cd C:\Coding\IDS_DETECTION\backend
.\demo_smartstay.ps1
```

**Features:**
- Runs all 5 attacks sequentially
- 3-second delays between attacks
- Colored output with progress tracking
- Automatic token setup

### Option 2: Quick Demo (No Delays)

```powershell
cd C:\Coding\IDS_DETECTION\backend
.\demo_smartstay_quick.ps1
```

**Features:**
- Fast execution (no delays)
- Perfect for time-limited demos

### Option 3: Manual Individual Attacks

```powershell
cd C:\Coding\IDS_DETECTION\backend
$env:IDS_API_TOKEN = "your-secure-token-here-change-in-production"

# Run individual attacks
python attack_dos.py 127.0.0.1 5000
python attack_ddos.py 127.0.0.1 5000
python attack_portscan.py 127.0.0.1 5000
python attack_bruteforce.py 127.0.0.1 5000
python attack_webattack.py 127.0.0.1 5000
```

---

## Attack Types & Targets

| Attack Type | Target Port | SmartStay Endpoint | Detection Confidence |
|-------------|-------------|-------------------|---------------------|
| **DoS** | 5000 | `/health` | 99% |
| **DDoS** | 5000 | `/api/ai/chatbot` | 97% |
| **Port Scan** | Multiple | Infrastructure | 95% |
| **Brute Force** | 5000 | Auth System | 94% |
| **Web Attack** | 5000 | `/api/ai/chatbot`, `/api/reports` | 94% |

---

## What to Show During Demo

### Phase 1: Normal Operation (15 seconds)
1. Open SmartStay frontend: http://localhost:8080
2. Open IDS dashboard: http://localhost:5173
3. Explain: "SmartStay is a PG booking platform protected by our IDS"

### Phase 2: Attack Demo (2-3 minutes)

**Run the demo script:**
```powershell
cd C:\Coding\IDS_DETECTION\backend
.\demo_smartstay.ps1
```

**While attacks are running:**
1. Switch between IDS dashboard and terminal
2. Point out real-time detections appearing
3. Highlight AI-generated mitigation suggestions
4. Explain attack types as they occur

### Phase 3: Review Results (30 seconds)
1. Open IDS "Threats" page
2. Show all detected attacks with details
3. Highlight confidence scores (94-99%)
4. Explain mitigation strategies

---

## Important Notes

### ✅ Safe Targets (OK to attack)
- `/health` - Health check endpoint
- `/api/ai/chatbot` - AI chatbot
- `/api/recently-viewed` - Recently viewed properties
- `/api/reports` - Reports endpoint
- Port scanning (no actual requests)

### ❌ NOT Targeted (Protected)
- Authentication endpoints (connected to Supabase)
- User profile management
- Database operations

### 🔒 Security
- All attacks are **localhost only** (127.0.0.1)
- No external network traffic
- Safe for classroom/workshop demos
- Educational use only

---

## Troubleshooting

### ❌ "Module 'scapy' not found"
```powershell
cd C:\Coding\IDS_DETECTION\backend
.\.venv\Scripts\Activate.ps1
pip install scapy
```

### ❌ "Permission denied" (Packet capture)
**Solution**: Run PowerShell as Administrator

### ❌ IDS shows "401 Unauthorized"
```powershell
$env:IDS_API_TOKEN = "your-secure-token-here-change-in-production"
```

### ❌ SmartStay not responding
1. Check if Flask is running: `netstat -ano | findstr :5000`
2. Restart SmartStay backend
3. Verify port 5000 is free

### ❌ IDS dashboard not updating
1. Check IDS backend: http://127.0.0.1:8000/
2. Verify API token is set
3. Check browser console (F12) for errors
4. Refresh IDS frontend

---

## Demo Timing

| Activity | Duration |
|----------|----------|
| Setup explanation | 30 seconds |
| Normal operation demo | 15 seconds |
| Running attacks (automated) | 60 seconds |
| Results review | 30 seconds |
| Q&A buffer | 45 seconds |
| **Total** | **3 minutes** |

---

## Expected Results

### Attack Detection Summary
- ✅ 5 attacks detected
- ✅ 94-99% confidence scores
- ✅ AI-generated mitigation suggestions
- ✅ Real-time dashboard updates
- ✅ Complete threat logs in "Threats" page

### Dashboard Behavior
- **Main Dashboard**: Shows last 500 events (normal + attacks)
- **Threats Page**: Shows last 1,000 attacks only
- **Circular Buffer**: Auto-removes oldest entries
- **Real-time**: Updates within 1 second of attack

---

## Complete Documentation

For detailed information, see:
- [SMARTSTAY_DEMO_GUIDE.md](SMARTSTAY_DEMO_GUIDE.md) - Complete integration guide
- [SETUP.md](SETUP.md) - Installation and configuration
- [backend/DEMO_GUIDE.md](backend/DEMO_GUIDE.md) - Standalone IDS demo
- [README.md](README.md) - Project overview

---

## Pre-Demo Checklist

Before presenting, verify:

- [ ] SmartStay backend running (http://127.0.0.1:5000)
- [ ] SmartStay frontend running (http://localhost:8080)
- [ ] IDS backend running (http://127.0.0.1:8000)
- [ ] IDS frontend running (http://localhost:5173)
- [ ] API token set: `$env:IDS_API_TOKEN`
- [ ] PowerShell as Administrator
- [ ] Browser tabs arranged
- [ ] Virtual environments activated
- [ ] Demo script practiced

---

**Ready to demo? Run:**
```powershell
cd C:\Coding\IDS_DETECTION\backend
.\demo_smartstay.ps1
```

**Good luck! 🎉**
