@echo off
setlocal

call "file remover.bat"

REM Run Abaqus CAE script
abaqus cae nogui="main.py"

endlocal