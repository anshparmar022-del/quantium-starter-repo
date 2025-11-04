Write-Host "🚀 Activating virtual environment..."
& "venv/Scripts/Activate.ps1"

Write-Host "✅ Running test suite..."
pytest test_app.py
$exitCode = $LASTEXITCODE  # capture the numeric exit code from pytest

if ($exitCode -eq 0) {
    Write-Host "🎉 All tests passed successfully!"
    deactivate
    exit 0
} else {
    Write-Host "❌ Some tests failed!"
    deactivate
    exit 1
}
