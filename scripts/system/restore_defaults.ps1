powercfg -setactive SCHEME_BALANCED 2>$null
Set-Service -Name SysMain -StartupType Automatic -ErrorAction SilentlyContinue
Set-Service -Name DiagTrack -StartupType Automatic -ErrorAction SilentlyContinue
Set-Service -Name dmwappushservice -StartupType Automatic -ErrorAction SilentlyContinue
Write-Host "Default settings restored."
Read-Host "Press Enter to continue"