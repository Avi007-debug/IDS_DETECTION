# 🛠️ Setup Guide

Complete installation and configuration guide for the Multi-Stage Intrusion Detection System.

## Prerequisites

### Required Software
- **Python 3.8+**: [Download](https://www.python.org/downloads/)
- **Node.js 16+**: [Download](https://nodejs.org/)
- **Npcap** (Windows): [Download](https://npcap.com/#download) - Required for packet capture

### System Requirements
- Windows 10/11 (or Linux/macOS with appropriate modifications)
- Administrator privileges for packet capture
- Minimum 4GB RAM
- 500MB free disk space

## Installation Steps

### 1. Clone the Repository

```powershell
git clone https://github.com/Avi007-debug/IDS_DETECTION
cd IDS_DETECTION
```

### 2. Backend Setup

#### Create Virtual Environment

```powershell
cd backend
python -m venv .venv
```

#### Activate Virtual Environment

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# If you get an execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

#### Install Dependencies

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Frontend Setup

```powershell
cd ../frontend
npm install
```

## Running the System

### Set API Token (Important!)

Set the API token before starting the backend:

```powershell
# Windows PowerShell
$env:IDS_API_TOKEN = "your-secure-token-here-change-in-production"
echo $env:IDS_API_TOKEN

#for cmd.exe
set IDS_API_TOKEN=your-secure-token-here-change-in-production
echo %IDS_API_TOKEN%

# Or set permanently in your environment variables
[Environment]::SetEnvironmentVariable("IDS_API_TOKEN", "your-secure-token-here", "User")
```

> ⚠️ **For demos**: Use the default token or set `$env:IDS_API_TOKEN` before running attacks

### Start Backend API

Open PowerShell in the `backend` directory:

```powershell
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

**Verify**: Visit http://127.0.0.1:8000/ - you should see `{"status": "IDS backend running"}`

### Start Real-Time Sensor (Optional)

**Important**: Run PowerShell as Administrator

#### Option 1: General Network Monitor (All Traffic)

Monitors all network traffic on all ports:

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python -c "from app.realtime.sniffer import start_sniffing; start_sniffing()"
```

#### Option 2: SmartStay Network Monitor (Ports 5000, 8080)

Monitors only SmartStay traffic and reports to the same IDS dashboard:

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python -c "from app.realtime.sniffer_smartstay import start_sniffing_smartstay; start_sniffing_smartstay()"
```

This option:
- ✅ Filters traffic to SmartStay ports only (5000, 8080)
- ✅ Reports attacks to same IDS frontend (http://localhost:5173)
- ✅ Adds [SmartStay] prefix to detection messages
- ✅ Focuses monitoring on your PG booking application

> ⚠️ **IMPORTANT**: When using SmartStay monitor, you MUST run attacks with port 5000:
> ```powershell
> python attack_dos.py 127.0.0.1 5000    # ✅ Will be detected
> python attack_dos.py 127.0.0.1         # ❌ Won't be detected (uses port 80)
> ```

### Start Frontend Dashboard

Open a new terminal in the `frontend` directory:

```powershell
npm run dev
```

**Access**: Open http://localhost:5173 in your browser

## Testing the System

### Understanding Data Storage

The system uses two circular buffers:
- **Dashboard (All Events)**: Stores last 500 detections (both normal and attacks)
- **Threats Page**: Stores last 1,000 attacks only

When limits are reached, oldest entries are automatically removed (FIFO - First In, First Out).

### Generate Normal Traffic

```powershell
ping 8.8.8.8 -t
```

Watch the dashboard show "Normal" classifications.

### Simulate Attacks

**Important**: Set the API token before running attacks:

```powershell
$env:IDS_API_TOKEN = "your-secure-token-here-change-in-production"
```

Then run individual attack scripts:

```powershell
cd backend

# For generic demo (default target: 127.0.0.1:80)
python attack_dos.py 127.0.0.1
python attack_ddos.py 127.0.0.1
python attack_portscan.py 127.0.0.1
python attack_bruteforce.py 127.0.0.1
python attack_webattack.py 127.0.0.1

# For SmartStay demo (target: 127.0.0.1:5000)
# ⚠️ MUST use port 5000 if SmartStay monitor is running!
python attack_dos.py 127.0.0.1 5000
python attack_ddos.py 127.0.0.1 5000
python attack_portscan.py 127.0.0.1 5000
python attack_bruteforce.py 127.0.0.1 5000
python attack_webattack.py 127.0.0.1 5000

# OR use the SmartStay automated demo script
.\demo_smartstay.ps1

# OR use the unified demo script (generic, not SmartStay)
python demo_attack.py 127.0.0.1 dos
python demo_attack.py 127.0.0.1 ddos
python demo_attack.py 127.0.0.1 portscan
python demo_attack.py 127.0.0.1 bruteforce
python demo_attack.py 127.0.0.1 webattack
```

Observe attack alerts in the dashboard with AI-generated mitigation suggestions.

### Testing SmartStay Network Monitor

If you're running the **SmartStay Network Monitor** (Option 2 above), follow these steps:

#### 1. Generate Normal SmartStay Traffic

Open SmartStay in your browser and interact with it:

```powershell
# Open in browser: http://localhost:8080
# Click around, use the chatbot, search for properties
# You should see normal traffic in the monitor terminal
```

Or test API endpoints directly:

```powershell
# Test SmartStay health endpoint
curl http://127.0.0.1:5000/health

# Test SmartStay AI chatbot
curl -X POST http://127.0.0.1:5000/api/ai/chatbot `
  -H "Content-Type: application/json" `
  -d '{\"message\":\"Hello\"}'
```

Watch the SmartStay monitor terminal show traffic like:
```
=== SmartStay FLOW DETECTED [2026-01-22 15:45:30] ===
Flow: 127.0.0.1:xxxxx -> 127.0.0.1:5000 (TCP)
Attack Type: Normal (Confidence: 0.95)
Suggestion: [SmartStay] Safe: Normal traffic pattern
```

#### 2. Simulate Attacks on SmartStay

**Important**: Use port 5000 for all attacks:

```powershell
cd backend
$env:IDS_API_TOKEN = "your-secure-token-here-change-in-production"

# Individual attacks
python attack_dos.py 127.0.0.1 5000
python attack_ddos.py 127.0.0.1 5000
python attack_portscan.py 127.0.0.1 5000
python attack_bruteforce.py 127.0.0.1 5000
python attack_webattack.py 127.0.0.1 5000

# OR automated demo
.\demo_smartstay.ps1
```

Watch the SmartStay monitor detect attacks in real-time with **[SmartStay]** prefix!

---

## Troubleshooting

### Scapy Issues (Windows)
- Install Npcap with "WinPcap API-compatible Mode" enabled
- Run PowerShell as Administrator
- Verify network adapter is enabled

### Virtual Environment Activation
If `.venv\Scripts\Activate.ps1` fails:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

### Port Already in Use
Change the port in the uvicorn command:
```powershell
uvicorn app.main:app --reload --port 8001
```

### Frontend Build Issues
```powershell
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

## Project URLs

- **Backend API**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs
- **Frontend**: http://localhost:5173

## Next Steps

1. Review [backend/DEMO_GUIDE.md](backend/DEMO_GUIDE.md) for presentation tips
2. **NEW**: Check [SMARTSTAY_DEMO_GUIDE.md](SMARTSTAY_DEMO_GUIDE.md) for SmartStay integration demo
3. Check [IDS_final.ipynb](IDS_final.ipynb) to understand model training
4. Explore the REST API at http://127.0.0.1:8000/docs
