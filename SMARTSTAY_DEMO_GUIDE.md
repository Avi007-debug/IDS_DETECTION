# 🏨 SmartStay IDS Integration - Demo Guide

Complete guide for demonstrating the Multi-Stage Intrusion Detection System integrated with SmartStay application.

## 📋 Overview

This guide demonstrates how the IDS system protects SmartStay, a PG/hostel booking platform, from various cyber attacks in real-time.

**SmartStay Application:**
- **Backend**: Flask API with AI-powered features (Groq)
- **Frontend**: React + Vite dashboard
- **Features**: Sentiment analysis, chatbot, travel time estimation, property recommendations
- **Authentication**: Supabase (for signup/signin only - all other features work locally)

**IDS System:**
- **Backend**: FastAPI with ML-based intrusion detection
- **Frontend**: React dashboard showing real-time threats
- **Detection**: DoS, DDoS, Port Scan, Brute Force, Web Attacks

---

## 🎯 Demo Scenario

**Scenario**: SmartStay is under cyber attack from malicious actors attempting to:
1. Overwhelm the server (DoS/DDoS)
2. Discover vulnerabilities (Port Scanning)
3. Compromise user accounts (Brute Force)
4. Inject malicious code (SQL Injection/XSS)

The IDS system detects and reports these attacks in real-time with AI-generated mitigation strategies.

---

## 🚀 Quick Start

### Prerequisites
- ✅ SmartStay backend running on `http://127.0.0.1:5000`
- ✅ SmartStay frontend running on `http://localhost:8080`
- ✅ IDS backend running on `http://127.0.0.1:8000`
- ✅ IDS frontend running on `http://localhost:5173`
- ✅ Administrator privileges (for packet capture)

### System URLs

| Component | URL |
|-----------|-----|
| SmartStay Backend | http://127.0.0.1:5000 |
| SmartStay Frontend | http://localhost:8080 |
| IDS Backend API | http://127.0.0.1:8000 |
| IDS API Docs | http://127.0.0.1:8000/docs |
| IDS Dashboard | http://localhost:5173 |

---

## 📝 Pre-Demo Setup

### 1. Start SmartStay Backend

```powershell
cd C:\Coding\SmartStay\backend
.\venv\Scripts\Activate.ps1
python app.py
```

**Expected Output:**
```
Starting SmartStay AI Backend...
AI provider configured: True (provider=groq)
✅ AI provider initialized successfully
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.0.104:5000
```

### 2. Start SmartStay Frontend

```powershell
cd C:\Coding\SmartStay\frontend
npm run dev
```

**Expected Output:**
```
VITE v5.4.19  ready in 1263 ms
➜  Local:   http://localhost:8080/
```

### 3. Start IDS Backend

```powershell
cd C:\Coding\IDS_DETECTION\backend
.\.venv\Scripts\Activate.ps1

# Set API token (IMPORTANT!)
$env:IDS_API_TOKEN = "your-secure-token-here-change-in-production"

# Start backend
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

**Verify**: Visit http://127.0.0.1:8000/ - should see `{"status": "IDS backend running"}`

### 4. Start IDS Frontend

```powershell
cd C:\Coding\IDS_DETECTION\frontend
npm run dev
```

**Access**: http://localhost:5173

### 5. (Optional) Start Real-Time SmartStay Monitor

For live packet capture and real-time detection (Run as Administrator):

```powershell
cd C:\Coding\IDS_DETECTION\backend
.\.venv\Scripts\Activate.ps1

# Option A: SmartStay-specific monitor (ports 5000, 8080 only)
python -c "from app.realtime.sniffer_smartstay import start_sniffing_smartstay; start_sniffing_smartstay()"

# Option B: General network monitor (all traffic)
python -c "from app.realtime.sniffer import start_sniffing; start_sniffing()"
```

**Benefits of SmartStay-specific monitor:**
- ✅ Filters only SmartStay traffic
- ✅ Reduces noise from other network activity
- ✅ Adds [SmartStay] context to detections
- ✅ Perfect for focused demonstrations

---

## 🎬 Demo Flow

### Phase 1: Normal Operation (Baseline)

1. **Show SmartStay in Action**
   - Open http://localhost:8080
   - Navigate through the app (search, chatbot, etc.)
   - Explain: "SmartStay is a secure PG booking platform with AI features"

2. **Show IDS Dashboard**
   - Open http://localhost:5173
   - Show empty/normal state
   - Explain: "IDS monitors all network traffic to SmartStay"

### Phase 2: Attack Simulations

**⚠️ Important**: Set API token before running attacks!
```powershell
cd C:\Coding\IDS_DETECTION\backend
$env:IDS_API_TOKEN = "your-secure-token-here-change-in-production"
```

#### Attack 1: DoS (Denial of Service)

**Purpose**: Overwhelm SmartStay's health check endpoint

```powershell
python attack_dos.py 127.0.0.1 5000
```

**What to Show:**
- Terminal: Packet flood progress
- IDS Dashboard: Real-time detection appears
- Attack Type: "DoS"
- Confidence: 99%
- AI Suggestion: "SmartStay under DoS attack! Enable rate limiting on port 5000..."

**Duration**: ~5 seconds

---

#### Attack 2: DDoS (Distributed Denial of Service)

**Purpose**: Coordinated attack from multiple IPs on SmartStay's chatbot API

```powershell
python attack_ddos.py 127.0.0.1 5000
```

**What to Show:**
- Terminal: Multiple source IPs attacking
- IDS Dashboard: Detects distributed nature
- Attack Type: "DDoS"
- Confidence: 97%
- AI Suggestion: "SmartStay under coordinated DDoS attack! Deploy DDoS mitigation..."
- Source IP: "multiple"

**Duration**: ~8 seconds

---

#### Attack 3: Port Scan

**Purpose**: Reconnaissance to discover SmartStay's open ports and services

```powershell
python attack_portscan.py 127.0.0.1 5000
```

**What to Show:**
- Terminal: Sequential port probing (5000, 8080, 443, 22, 3306, etc.)
- IDS Dashboard: Reconnaissance detected
- Attack Type: "PortScan"
- Confidence: 95%
- AI Suggestion: "SmartStay infrastructure being scanned! Implement port knocking..."

**Duration**: ~10 seconds

---

#### Attack 4: Brute Force

**Purpose**: Credential stuffing attack on SmartStay's authentication system

```powershell
python attack_bruteforce.py 127.0.0.1 5000
```

**What to Show:**
- Terminal: Rapid login attempts with common credentials
- IDS Dashboard: Authentication attack detected
- Attack Type: "BruteForce"
- Confidence: 94%
- AI Suggestion: "SmartStay authentication under brute force attack! Implement account lockout after 3 failed attempts..."

**Credentials Tested:**
- admin@smartstay.com:password123
- user@smartstay.com:12345678
- test@smartstay.com:test123
- (and more...)

**Duration**: ~12 seconds

---

#### Attack 5: Web Attack (SQL Injection & XSS)

**Purpose**: Inject malicious payloads into SmartStay's API endpoints

```powershell
python attack_webattack.py 127.0.0.1 5000
```

**What to Show:**
- Terminal: Malicious HTTP requests sent
- IDS Dashboard: Web attack detected
- Attack Type: "WebAttack"
- Confidence: 94%
- AI Suggestion: "SmartStay API under web attack (SQL Injection/XSS)! Enable WAF..."

**Malicious Payloads:**
- `' OR '1'='1` (SQL Injection)
- `<script>alert('XSS')</script>` (XSS)
- `';DROP TABLE pg_listings--` (SQL Injection)

**Targeted Endpoints:**
- `/api/ai/chatbot`
- `/api/recently-viewed`
- `/api/reports`
- `/health`

**Duration**: ~5 seconds

---

### Phase 3: Demo Script (All Attacks)

Run all attacks sequentially for a comprehensive demo:

```powershell
cd C:\Coding\IDS_DETECTION\backend
$env:IDS_API_TOKEN = "your-secure-token-here-change-in-production"

# Run all attacks
python attack_dos.py 127.0.0.1 5000
Start-Sleep -Seconds 3

python attack_ddos.py 127.0.0.1 5000
Start-Sleep -Seconds 3

python attack_portscan.py 127.0.0.1 5000
Start-Sleep -Seconds 3

python attack_bruteforce.py 127.0.0.1 5000
Start-Sleep -Seconds 3

python attack_webattack.py 127.0.0.1 5000
```

**Total Duration**: ~60 seconds

---

## 📊 IDS Dashboard Features

### Main Dashboard (All Events)
- **Capacity**: Last 500 detections (normal + attacks)
- **Display**: Real-time table with timestamp, source IP, attack type, confidence
- **Circular Buffer**: FIFO - oldest entries removed when limit reached

### Threats Page
- **Capacity**: Last 1,000 attacks only
- **Filter**: Only shows detected attacks (excludes normal traffic)
- **Details**: AI-generated mitigation suggestions for each attack

### Key Metrics
- Total attacks detected
- Attack type distribution
- Confidence scores
- Source IP tracking
- Target port analysis

---

## 🎤 Presentation Script

### Introduction (30 seconds)
"SmartStay is a PG booking platform with AI-powered features like sentiment analysis, chatbot assistance, and travel time estimation. Today, we'll demonstrate how our Multi-Stage Intrusion Detection System protects SmartStay from cyber attacks in real-time."

### Demo (2-3 minutes)
1. **Show Normal Operation** (20 seconds)
   - "Here's SmartStay running normally on localhost:8080"
   - "Our IDS is monitoring all network traffic on port 5000"

2. **Simulate DoS Attack** (15 seconds)
   - "Let's simulate a DoS attack flooding the health endpoint"
   - "Notice: IDS immediately detects the attack with 99% confidence"
   - "AI suggests: Enable rate limiting and block the source IP"

3. **Simulate DDoS Attack** (15 seconds)
   - "Now a coordinated DDoS from multiple IPs targeting the chatbot API"
   - "IDS identifies the distributed nature of the attack"
   - "AI recommends: Deploy Cloudflare DDoS protection"

4. **Simulate Port Scan** (15 seconds)
   - "An attacker is scanning for vulnerabilities"
   - "IDS detects reconnaissance activity"
   - "AI suggests: Close unused ports, enable IDS/IPS rules"

5. **Simulate Brute Force** (15 seconds)
   - "Credential stuffing attack on authentication"
   - "IDS catches rapid login attempts"
   - "AI recommends: Account lockout, 2FA, CAPTCHA"

6. **Simulate Web Attack** (15 seconds)
   - "SQL injection and XSS attempts on API endpoints"
   - "IDS detects malicious payloads"
   - "AI suggests: Enable WAF, validate inputs"

7. **Show Threats Dashboard** (20 seconds)
   - "All attacks logged with mitigation strategies"
   - "Security team can respond immediately"

### Conclusion (30 seconds)
"Our IDS provides real-time protection for SmartStay by detecting attacks with 94-99% confidence and providing actionable AI-generated mitigation strategies. This multi-stage approach ensures SmartStay remains secure while serving legitimate users."

---

## ⚠️ Important Notes

### Authentication Considerations
- **Supabase Connection**: SmartStay's signup/signin uses Supabase (external service)
- **Safe Testing**: Attack scripts target non-authentication endpoints to avoid impacting Supabase
- **Local Testing**: All other SmartStay features work locally without Supabase dependency

### Legal Endpoints Targeted
✅ **Safe to attack (local endpoints):**
- `/health` - Health check (DoS target)
- `/api/ai/chatbot` - AI chatbot (DDoS, Web Attack target)
- `/api/recently-viewed` - Recently viewed properties (Web Attack target)
- `/api/reports` - Reports endpoint (Web Attack target)
- Port scanning (reconnaissance, no actual requests)

❌ **NOT targeted (Supabase-dependent):**
- Authentication endpoints (signup/signin)
- User profile management
- Database operations requiring auth

### Network Safety
- All attacks use **localhost (127.0.0.1)** - no external targets
- Scapy sends packets locally - no internet traffic
- IDS reports to local backend (127.0.0.1:8000)
- Safe for classroom/workshop demos

### Performance Considerations
- **Packet Rate**: Deliberately slowed (0.05-0.15s delays) to prevent overwhelming demo systems
- **Buffer Limits**: Dashboard shows last 500 events, Threats shows last 1,000 attacks
- **Resource Usage**: Minimal CPU/memory impact during demo

---

## 🐛 Troubleshooting

### Issue: "No module named 'scapy'"
```powershell
cd C:\Coding\IDS_DETECTION\backend
.\.venv\Scripts\Activate.ps1
pip install scapy
```

### Issue: "Permission denied" on packet capture
**Solution**: Run PowerShell as Administrator

### Issue: IDS backend shows 401 Unauthorized
**Solution**: Set API token before attacks
```powershell
$env:IDS_API_TOKEN = "your-secure-token-here-change-in-production"
```

### Issue: SmartStay backend not responding
**Check**:
1. Is Flask running? Look for "Running on http://127.0.0.1:5000"
2. Is port 5000 free? Run: `netstat -ano | findstr :5000`
3. Restart SmartStay backend

### Issue: IDS dashboard not showing attacks
**Check**:
1. Is IDS backend running? Visit http://127.0.0.1:8000/
2. Is API token set correctly?
3. Check browser console for errors (F12)

### Issue: SmartStay frontend shows auth errors
**Note**: Signup/signin requires internet (Supabase). For demo purposes:
- Use existing test account OR
- Skip auth features (chatbot, search work without login)

---

## 📈 Expected Results

### Attack Detection Rates
- **DoS**: 99% confidence (high packet rate on single port)
- **DDoS**: 97% confidence (multiple source IPs detected)
- **PortScan**: 95% confidence (sequential port probing pattern)
- **BruteForce**: 94% confidence (rapid authentication attempts)
- **WebAttack**: 94% confidence (SQL injection/XSS payloads detected)

### Response Times
- Detection: < 1 second after attack starts
- Dashboard update: Real-time (WebSocket)
- AI suggestion generation: < 2 seconds

### Dashboard Behavior
- **Main Dashboard**: Shows all traffic (normal + attacks)
- **Circular Buffer**: Automatically removes oldest entries beyond 500
- **Threats Page**: Filters to show only attacks (max 1,000)
- **Persistence**: In-memory only (resets on backend restart)

---

## 🎓 Educational Value

### Learning Objectives
1. **Network Security**: Understanding common attack vectors
2. **Intrusion Detection**: Real-time threat monitoring
3. **AI/ML in Security**: Automated threat analysis and mitigation
4. **Incident Response**: Actionable security recommendations
5. **Web Application Security**: Protecting APIs and endpoints

### Technical Concepts Demonstrated
- Packet-level network analysis (Scapy)
- Machine learning for anomaly detection
- REST API security patterns
- Real-time data streaming
- Threat intelligence automation

---

## 📚 Additional Resources

### Project Documentation
- [SETUP.md](SETUP.md) - Full installation guide
- [DEMO_GUIDE.md](backend/DEMO_GUIDE.md) - IDS standalone demo
- [README.md](README.md) - Project overview
- [EXPLAINABILITY.md](EXPLAINABILITY.md) - Model interpretability

### SmartStay Documentation
- [README.md](../SmartStay/README.md) - SmartStay project overview
- [FEATURES.md](../SmartStay/FEATURES.md) - Feature documentation
- [TEST_API.md](../SmartStay/backend/TEST_API.md) - API testing guide

### Demo Variations
1. **Quick Demo** (1 minute): Run 1-2 attacks, show dashboard
2. **Full Demo** (3 minutes): Run all 5 attacks with explanations
3. **Interactive Demo** (5 minutes): Let audience suggest attack types
4. **Technical Deep Dive** (10 minutes): Explain ML models, feature extraction

---

## 🔒 Security Disclaimer

**⚠️ EDUCATIONAL USE ONLY**

This demonstration simulates cyber attacks in a controlled, local environment for educational purposes. The attack scripts:
- Only target localhost (127.0.0.1)
- Do NOT send packets to external networks
- Are designed for learning, NOT malicious use
- Should NEVER be used against systems you don't own

**Legal Notice**: Unauthorized use of these scripts against third-party systems is illegal and may result in criminal prosecution under computer fraud and abuse laws.

---

## 📞 Support

**Issues or Questions?**
- Check [Troubleshooting](#-troubleshooting) section
- Review [SETUP.md](SETUP.md) for configuration help
- Verify all prerequisites are met
- Ensure API token is set correctly

**Demo Tips:**
- Practice the demo flow 2-3 times before presenting
- Have backup terminals ready in case one fails
- Keep browser windows arranged for easy switching
- Prepare to explain each attack type briefly

---

## ✅ Pre-Demo Checklist

- [ ] SmartStay backend running on port 5000
- [ ] SmartStay frontend running on port 8080
- [ ] IDS backend running on port 8000
- [ ] IDS frontend running on port 5173
- [ ] API token set in environment: `$env:IDS_API_TOKEN`
- [ ] PowerShell running as Administrator (for packet capture)
- [ ] All browser tabs open and arranged
- [ ] Virtual environments activated
- [ ] Network connectivity verified
- [ ] Demo script practiced

---

**Last Updated**: January 2026  
**Version**: 1.0  
**Compatibility**: Windows 10/11, SmartStay v1.0, IDS v1.0
