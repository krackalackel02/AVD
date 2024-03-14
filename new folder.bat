@echo off
setlocal enabledelayedexpansion

:: Initialize variables to store the max numbers
set /a maxMajor=0
set /a maxMinor=-1

:: Loop through the directories to find the highest iter X_Y
for /d %%D in (iter*) do (
    set "dirName=%%~nD"
    for /f "tokens=2,3 delims=_ " %%a in ("!dirName!") do (
        set /a majorNum=%%a
        set /a minorNum=%%b
        if !majorNum! geq !maxMajor! (
            if !minorNum! gtr !maxMinor! (
                set /a maxMajor=!majorNum!
                set /a maxMinor=!minorNum!
            )
        )
    )
)

:: Increment the minor iteration number for the new folder
set /a newMinor=%maxMinor%+1

:: Create the new iteration folder and the Geometry subfolder
set "newFolder=iter %maxMajor%_%newMinor%"
mkdir "%newFolder%\Geometry"

echo New folder created: %newFolder% with a Geometry subfolder