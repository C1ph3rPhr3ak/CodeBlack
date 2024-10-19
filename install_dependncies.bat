@echo off

:: Check if adb is installed
where adb >nul 2>&1
if %errorlevel% neq 0 (
	echo adb not found. Installing Android SDK Platform Tools...
	choco install adb -y
)

:: Check if tcpdump is installed
where tcpdump >nul 2>&1
if %errorlevel% new 0 (
	echo tcpdump not found. Installing...
	choco install tcpdump -y
)

:: Install Python dependencies
pip install -r requirements.txt
