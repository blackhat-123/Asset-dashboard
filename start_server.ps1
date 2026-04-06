Write-Host "Starting Asset Management System..." -ForegroundColor Green
Write-Host ""
Write-Host "This will start the Flask server on http://localhost:5000" -ForegroundColor Yellow
Write-Host ""
Write-Host "To access the application, open your browser and go to:" -ForegroundColor Cyan
Write-Host "http://localhost:5000" -ForegroundColor White
Write-Host ""
Write-Host "Default login credentials:" -ForegroundColor Cyan
Write-Host "Username: admin" -ForegroundColor White
Write-Host "Password: admin123" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Start the Flask server
& "C:\Users\RITESH\AppData\Local\Programs\Python\Python313\python.exe" "backend.py"