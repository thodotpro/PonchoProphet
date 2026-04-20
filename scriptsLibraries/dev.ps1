# =============================================================
# dev.ps1 — run this every time you want to work on the project
# Activates the Python venv AND starts Docker
# Run from a PowerShell terminal: .\dev.ps1
# =============================================================

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "=== Outfit Agent — Starting dev environment ===" -ForegroundColor Cyan
Write-Host ""

# -------------------------------------------------------------
# Check that .env exists
# Docker Compose reads this file for API keys and config.
# If it is missing, the backend container will crash on startup.
# -------------------------------------------------------------
if (-not (Test-Path ".env")) {
    Write-Host "ERROR: .env file not found." -ForegroundColor Red
    Write-Host "Copy .env.example to .env and fill in your API keys:" -ForegroundColor Yellow
    Write-Host "  Copy-Item .env.example .env" -ForegroundColor White
    exit 1
}

# -------------------------------------------------------------
# Check that Docker is running
# Docker Desktop must be open before this will work
# -------------------------------------------------------------
Write-Host "Checking Docker..." -ForegroundColor Yellow
try {
    docker info 2>&1 | Out-Null
    Write-Host "Docker is running." -ForegroundColor Green
} catch {
    Write-Host "ERROR: Docker is not running." -ForegroundColor Red
    Write-Host "Open Docker Desktop and wait for it to finish starting." -ForegroundColor Yellow
    exit 1
}

# -------------------------------------------------------------
# Activate the Python virtual environment
# This is for your terminal session — lets you run Python
# scripts and tests locally without going through Docker
# -------------------------------------------------------------
Write-Host "Activating Python virtual environment..." -ForegroundColor Yellow

if (-not (Test-Path "backend\.venv")) {
    Write-Host "ERROR: backend\.venv not found." -ForegroundColor Red
    Write-Host "Run .\setup.ps1 first." -ForegroundColor Yellow
    exit 1
}

backend\.venv\Scripts\activate
Write-Host "Virtual environment active. (You will see (.venv) in your prompt)" -ForegroundColor Green

# -------------------------------------------------------------
# Start Docker Compose
# This builds images if needed and starts all three containers:
#   - redis      (the database/cache server)
#   - backend    (FastAPI + LangGraph)
#   - frontend   (Vue + Vite dev server)
#
# Logs from all three services stream here in real time.
# Press Ctrl+C to stop all containers.
# -------------------------------------------------------------
Write-Host ""
Write-Host "Starting Docker containers..." -ForegroundColor Yellow
Write-Host "  Redis:    (internal, no browser URL)" -ForegroundColor DarkGray
Write-Host "  Backend:  http://localhost:8000" -ForegroundColor DarkGray
Write-Host "  Backend docs: http://localhost:8000/docs" -ForegroundColor DarkGray
Write-Host "  Frontend: http://localhost:5173" -ForegroundColor DarkGray
Write-Host ""
Write-Host "Press Ctrl+C to stop everything." -ForegroundColor DarkGray
Write-Host ""

docker compose up

