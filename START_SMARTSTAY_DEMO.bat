@echo off
REM ============================================
REM SmartStay IDS Demo - Quick Start Launcher
REM ============================================
echo.
echo ========================================
echo    SmartStay IDS Integration Demo
echo ========================================
echo.
echo This script will help you start the demo.
echo.
echo Prerequisites:
echo   1. SmartStay backend running on port 5000
echo   2. SmartStay frontend running on port 8080
echo   3. IDS backend running on port 8000
echo   4. IDS frontend running on port 5173
echo.
pause
echo.
echo Starting attack demo...
echo.
cd /d "%~dp0backend"
powershell -ExecutionPolicy Bypass -File demo_smartstay.ps1
pause
