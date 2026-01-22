# ============================================
# SmartStay Attack Demo Script
# ============================================
# This script runs all attack simulations against SmartStay
# Target: SmartStay Backend (127.0.0.1:5000)
# ============================================

Write-Host "`n" -NoNewline
Write-Host "╔═══════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                                                           ║" -ForegroundColor Cyan
Write-Host "║        SmartStay IDS Integration - Attack Demo           ║" -ForegroundColor Cyan
Write-Host "║                                                           ║" -ForegroundColor Cyan
Write-Host "╚═══════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Configuration
$TARGET_IP = "127.0.0.1"
$TARGET_PORT = 5000
$DELAY_BETWEEN_ATTACKS = 3

# Check if API token is set
$apiToken = $env:IDS_API_TOKEN
if (-not $apiToken) {
    Write-Host "[!] WARNING: IDS_API_TOKEN not set!" -ForegroundColor Yellow
    Write-Host "[!] Setting default token..." -ForegroundColor Yellow
    $env:IDS_API_TOKEN = "your-secure-token-here-change-in-production"
}

Write-Host "[*] Target: SmartStay Backend" -ForegroundColor Green
Write-Host "[*] IP: $TARGET_IP" -ForegroundColor Green
Write-Host "[*] Port: $TARGET_PORT" -ForegroundColor Green
Write-Host "[*] API Token: Set" -ForegroundColor Green
Write-Host ""

# Ensure we're in the backend directory
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "Starting Attack Sequence..." -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Attack 1: DoS
Write-Host "[1/5] Launching DoS Attack..." -ForegroundColor Magenta
python attack_dos.py $TARGET_IP $TARGET_PORT
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ DoS Attack completed" -ForegroundColor Green
} else {
    Write-Host "✗ DoS Attack failed" -ForegroundColor Red
}
Write-Host ""
Start-Sleep -Seconds $DELAY_BETWEEN_ATTACKS

# Attack 2: DDoS
Write-Host "[2/5] Launching DDoS Attack..." -ForegroundColor Magenta
python attack_ddos.py $TARGET_IP $TARGET_PORT
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ DDoS Attack completed" -ForegroundColor Green
} else {
    Write-Host "✗ DDoS Attack failed" -ForegroundColor Red
}
Write-Host ""
Start-Sleep -Seconds $DELAY_BETWEEN_ATTACKS

# Attack 3: Port Scan
Write-Host "[3/5] Launching Port Scan..." -ForegroundColor Magenta
python attack_portscan.py $TARGET_IP $TARGET_PORT
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Port Scan completed" -ForegroundColor Green
} else {
    Write-Host "✗ Port Scan failed" -ForegroundColor Red
}
Write-Host ""
Start-Sleep -Seconds $DELAY_BETWEEN_ATTACKS

# Attack 4: Brute Force
Write-Host "[4/5] Launching Brute Force Attack..." -ForegroundColor Magenta
python attack_bruteforce.py $TARGET_IP $TARGET_PORT
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Brute Force Attack completed" -ForegroundColor Green
} else {
    Write-Host "✗ Brute Force Attack failed" -ForegroundColor Red
}
Write-Host ""
Start-Sleep -Seconds $DELAY_BETWEEN_ATTACKS

# Attack 5: Web Attack
Write-Host "[5/5] Launching Web Attack..." -ForegroundColor Magenta
python attack_webattack.py $TARGET_IP $TARGET_PORT
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Web Attack completed" -ForegroundColor Green
} else {
    Write-Host "✗ Web Attack failed" -ForegroundColor Red
}
Write-Host ""

Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "Demo Complete!" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""
Write-Host "[*] Check IDS Dashboard at: http://localhost:5173" -ForegroundColor Yellow
Write-Host "[*] Check SmartStay at: http://localhost:8080" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
