$tempPath = $env:TEMP

Get-ChildItem -Path $tempPath -Directory | ForEach-Object {
    Remove-Item -Path $_.FullName -Recurse -Force -ErrorAction SilentlyContinue
}

Get-ChildItem -Path $tempPath -File | ForEach-Object {
    Remove-Item -Path $_.FullName -Force -ErrorAction SilentlyContinue
}