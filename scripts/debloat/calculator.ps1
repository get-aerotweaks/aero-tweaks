Get-AppxPackage Microsoft.WindowsCalculator | Remove-AppxPackage

Get-AppxPackage -Name "Microsoft.WindowsCalculator"  | Remove-AppxPackage -ErrorAction SilentlyContinue
Get-AppxProvisionedPackage -Online | Where-Object { $_.DisplayName -eq "Microsoft.WindowsCalculator" } | Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue


Get-WindowsCapability -Online | Where-Object { $_.Name -like "*Calculator*" } | Remove-WindowsCapability -Online -ErrorAction SilentlyContinue


$shortcutPath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Calculator.lnk"
if (Test-Path $shortcutPath) {
    Remove-Item -Path $shortcutPath -Force
}