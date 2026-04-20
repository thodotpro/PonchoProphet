# =============================================================
# setup.ps1 — run this ONCE after cloning the repository
# Right-click this file and select "Run with PowerShell"
# or run it from a PowerShell terminal: .\setup.ps1
# =============================================================

# Stop the script immediately if any command fails
$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "=== Outfit Agent — First-time setup ===" -ForegroundColor Cyan
Write-Host ""

# -------------------------------------------------------------
# Step 1: Allow PowerShell to run local scripts
# Without this, .venv\Scripts\activate will be blocked by Windows
# You only ever need to do this once on your machine
# -------------------------------------------------------------
Write-Host "[1/5] Setting PowerShell execution policy..." -ForegroundColor Yellow
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
Write-Host "      Done." -ForegroundColor Green

# -------------------------------------------------------------
# Step 2: Check that Python is installed
# If this fails, download Python from https://python.org
# Make sure to check "Add Python to PATH" during installation
# -------------------------------------------------------------
Write-Host "[2/5] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "      Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "      ERROR: Python not found." -ForegroundColor Red
    Write-Host "      Download it from https://python.org" -ForegroundColor Red
    Write-Host "      Make sure to check 'Add Python to PATH' during install." -ForegroundColor Red
    exit 1
}

# -------------------------------------------------------------
# Step 3: Check that Node.js is installed
# If this fails, download Node from https://nodejs.org (LTS version)
# -------------------------------------------------------------
Write-Host "[3/5] Checking Node.js installation..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version 2>&1
    $npmVersion  = npm --version 2>&1
    Write-Host "      Found Node: $nodeVersion  npm: $npmVersion" -ForegroundColor Green
} catch {
    Write-Host "      ERROR: Node.js not found." -ForegroundColor Red
    Write-Host "      Download the LTS version from https://nodejs.org" -ForegroundColor Red
    exit 1
}

# -------------------------------------------------------------
# Step 4: Create Python virtual environment and install packages
# .venv is created inside the backend/ folder
# All Python packages go here — NOT into your global Python
# -------------------------------------------------------------
Write-Host "[4/5] Setting up Python virtual environment..." -ForegroundColor Yellow

Set-Location backend

if (Test-Path ".venv") {
    Write-Host "      .venv already exists, skipping creation." -ForegroundColor DarkGray
} else {
    python -m venv .venv
    Write-Host "      Created .venv" -ForegroundColor Green
}

# Activate the virtual environment
.venv\Scripts\activate

# Upgrade pip first — old pip versions sometimes fail on newer packages
python -m pip install --upgrade pip --quiet

# Install all backend dependencies
pip install -r requirements.txt

Write-Host "      Backend packages installed." -ForegroundColor Green

# Deactivate so we return to a clean shell state
deactivate

Set-Location ..

# -------------------------------------------------------------
# Step 5: Install Node/Vue packages for the frontend
# npm install reads package.json and creates node_modules/
# This folder can be 200MB+ — it is in .gitignore, never commit it
# -------------------------------------------------------------
Write-Host "[5/5] Installing frontend Node packages..." -ForegroundColor Yellow

Set-Location frontend
npm install --silent
Set-Location ..

Write-Host "      Frontend packages installed." -ForegroundColor Green

# -------------------------------------------------------------
# Done
# -------------------------------------------------------------
Write-Host ""
Write-Host "=== Setup complete ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor White
Write-Host "  1. Copy .env.example to .env and fill in your API keys" -ForegroundColor White
Write-Host "  2. Run .\dev.ps1 to start the app" -ForegroundColor White
Write-Host ""
