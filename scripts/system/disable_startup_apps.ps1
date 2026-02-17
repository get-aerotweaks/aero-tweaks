$startupPath = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"
if (Test-Path $startupPath) {
    Remove-Item -Path "$startupPath\*.lnk" -Force -ErrorAction SilentlyContinue
}
Write-Host "Startup apps cleared from Startup folder."
Read-Host "Press Enter to continue"