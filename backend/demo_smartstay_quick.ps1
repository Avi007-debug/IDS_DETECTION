# ============================================
# SmartStay Quick Demo (No Delays)
# ============================================
# Fast attack sequence for quick demonstrations
# Target: SmartStay Backend (127.0.0.1:5000)
# ============================================

Write-Host "`n🚀 SmartStay IDS - Quick Demo`n" -ForegroundColor Cyan

$TARGET_IP = "127.0.0.1"
$TARGET_PORT = 5000

# Set token if not already set
if (-not $env:IDS_API_TOKEN) {
    $env:IDS_API_TOKEN = "your-secure-token-here-change-in-production"
}

$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

Write-Host "Running all attacks against SmartStay ($TARGET_IP:$TARGET_PORT)...`n" -ForegroundColor Yellow

python attack_dos.py $TARGET_IP $TARGET_PORT
python attack_ddos.py $TARGET_IP $TARGET_PORT
python attack_portscan.py $TARGET_IP $TARGET_PORT
python attack_bruteforce.py $TARGET_IP $TARGET_PORT
python attack_webattack.py $TARGET_IP $TARGET_PORT

Write-Host "`n✅ All attacks completed!" -ForegroundColor Green
Write-Host "📊 Check IDS Dashboard: http://localhost:5173`n" -ForegroundColor Yellow
