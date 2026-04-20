# =============================================================
# rebuild.ps1 — run this after changing requirements.txt
#               or package.json
#
# A normal "docker compose up" does NOT re-run pip install
# or npm install — it reuses the cached image layer.
# This script forces a full rebuild so new packages are picked up.
# =============================================================

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "=== Outfit Agent — Rebuilding Docker images ===" -ForegroundColor Cyan
Write-Host ""

# Which service to rebuild — default is both, pass "backend" or "frontend" as arg
$service = $args[0]

if ($service -eq "backend") {
    Write-Host "Rebuilding backend only..." -ForegroundColor Yellow
    docker compose build --no-cache backend
} elseif ($service -eq "frontend") {
    Write-Host "Rebuilding frontend only..." -ForegroundColor Yellow
    docker compose build --no-cache frontend
} else {
    Write-Host "Rebuilding all services..." -ForegroundColor Yellow
    docker compose build --no-cache
}

Write-Host ""
Write-Host "Rebuild complete. Run .\dev.ps1 to start." -ForegroundColor Green
Write-Host ""

