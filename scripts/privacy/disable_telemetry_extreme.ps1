Stop-Service -Name DiagTrack -ErrorAction SilentlyContinue
Set-Service -Name DiagTrack -StartupType Disabled -ErrorAction SilentlyContinue
Stop-Service -Name dmwappushservice -ErrorAction SilentlyContinue
Set-Service -Name dmwappushservice -StartupType Disabled -ErrorAction SilentlyContinue
