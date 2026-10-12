@echo off
title AgentStudio OS - 50 AI Agent Demos
cd /d "%~dp0"

echo ==========================================================
echo    Starting AgentStudio OS: 50 Real-Time AI Agent Demos   
echo ==========================================================

start "" cmd /c "timeout /t 2 /nobreak >nul & start http://localhost:8050"

"C:\Users\rajes\.local\bin\python3.14.exe" server.py
if %ERRORLEVEL% NEQ 0 (
    python server.py
)
pause
