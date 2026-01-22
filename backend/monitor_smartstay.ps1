# ============================================
# SmartStay Network Monitor - Quick Launcher
# ============================================
# Monitors SmartStay traffic (ports 5000, 8080)
# Reports to IDS Dashboard at http://localhost:5173
# ============================================

Write-Host "`n" -NoNewline
Write-Host "╔═══════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                                                           ║" -ForegroundColor Cyan
Write-Host "║       SmartStay Network Monitor - IDS Integration        ║" -ForegroundColor Cyan
Write-Host "║                                                           ║" -ForegroundColor Cyan
Write-Host "╚═══════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Check if running as Administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "[!] ERROR: This script requires Administrator privileges!" -ForegroundColor Red
    Write-Host "[!] Please right-click PowerShell and select 'Run as Administrator'" -ForegroundColor Red
    Write-Host ""
    pause
    exit 1
}

Write-Host "[✓] Running as Administrator" -ForegroundColor Green
Write-Host ""

# Check if API token is set
$apiToken = $env:IDS_API_TOKEN
if (-not $apiToken) {
    Write-Host "[!] WARNING: IDS_API_TOKEN not set!" -ForegroundColor Yellow
    Write-Host "[!] Setting default token..." -ForegroundColor Yellow
    $env:IDS_API_TOKEN = "your-secure-token-here-change-in-production"
    Write-Host "[✓] Token configured" -ForegroundColor Green
} else {
    Write-Host "[✓] API Token: Set" -ForegroundColor Green
}

Write-Host ""
Write-Host "[*] Monitor Configuration:" -ForegroundColor Cyan
Write-Host "    - SmartStay Backend: http://127.0.0.1:5000" -ForegroundColor White
Write-Host "    - SmartStay Frontend: http://localhost:8080" -ForegroundColor White
Write-Host "    - IDS Backend: http://127.0.0.1:8000" -ForegroundColor White
Write-Host "    - IDS Dashboard: http://localhost:5173" -ForegroundColor White
Write-Host ""
Write-Host "[*] Monitored Ports: 5000, 8080" -ForegroundColor Cyan
Write-Host "[*] Press Ctrl+C to stop monitoring" -ForegroundColor Yellow
Write-Host ""

# Navigate to backend directory
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

# Activate virtual environment and start sniffer
Write-Host "Starting SmartStay network monitor..." -ForegroundColor Green
Write-Host ""

& .\.venv\Scripts\python.exe -c "from app.realtime.sniffer_smartstay import start_sniffing_smartstay; start_sniffing_smartstay()"
