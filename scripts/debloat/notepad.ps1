Get-AppxPackage -Name "Microsoft.Notepad" -AllUsers | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue
Get-AppxProvisionedPackage -Online | Where-Object { $_.DisplayName -eq "Microsoft.Notepad" } | Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue


Get-WindowsCapability -Online | Where-Object { $_.Name -like "*Notepad*" } | Remove-WindowsCapability -Online -ErrorAction SilentlyContinue


$shortcutPath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk"
if (Test-Path $shortcutPath) {
    Remove-Item -Path $shortcutPath -Force
}