@echo off
setlocal

call "file remover.bat"

REM Run Abaqus CAE script
abaqus cae script="main.py"

endlocal