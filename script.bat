@echo off
setlocal enabledelayedexpansion

call "file remover.bat"

set /a maxMajor=0
set /a maxMinor=-1

:: Echo starting search
echo Searching for the latest iter_X_Y directory...

:: Loop through the directories to find the highest iter X_Y
for /d %%D in (iter*) do (
    set "dirName=%%~nD"
    for /f "tokens=2,3 delims=_ " %%a in ("!dirName!") do (
        set /a majorNum=%%a
        set /a minorNum=%%b
        if !majorNum! geq !maxMajor! (
            if !majorNum! gtr !maxMajor! (
                set /a maxMajor=!majorNum!
                set /a maxMinor=!minorNum!
            ) else if !minorNum! gtr !maxMinor! (
                set /a maxMinor=!minorNum!
            )
        )
    )
)

set "newFolder=iter %maxMajor%_%maxMinor%"

:: Debugging line before running Abaqus to ensure the correct folder is passed
echo Running Abaqus with folder: %newFolder%

REM Uncomment the following line once debugging is complete and you're sure the correct folder is passed
abaqus cae script="main.py" -- "NO PLOT" "%newFolder%"

endlocal
