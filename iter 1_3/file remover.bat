@echo off
setlocal

REM Delete residual files using PowerShell, excluding the batch file
powershell -Command "& { Get-ChildItem | Where-Object { $_.Extension -ne '.bat' -and $_.Extension -ne '.py' -and $_.Name -notin @('keep file.txt') } | Remove-Item -Force }"

endlocal