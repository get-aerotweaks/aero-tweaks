Get-AppxPackage -Name "Microsoft.Paint" -AllUsers | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue
Get-AppxProvisionedPackage -Online | Where-Object { $_.DisplayName -eq "Microsoft.Paint" } | Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue


Get-WindowsCapability -Online | Where-Object { $_.Name -like "*Paint*" } | Remove-WindowsCapability -Online -ErrorAction SilentlyContinue


$shortcutPath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Paint.lnk"
if (Test-Path $shortcutPath) {
    Remove-Item -Path $shortcutPath -Force
}