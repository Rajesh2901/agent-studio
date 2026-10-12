# AgentStudio OS - PowerShell One-Click Launcher
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   Starting AgentStudio OS: 50 Real-Time AI Agent Demos   " -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan

# Find python
$pythonPath = "C:\Users\rajes\.local\bin\python3.14.exe"
if (-not (Test-Path $pythonPath)) {
    $pythonPath = "python"
}

# Launch browser after a short delay in background
Start-Job -ScriptBlock {
    Start-Sleep -Seconds 2
    Start-Process "http://localhost:8050"
} | Out-Null

# Start server
& $pythonPath "$scriptDir\server.py"
