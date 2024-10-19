#!/bin/bash

# Install system dependencies
sudo apt update

# Check and install adb (Android SDK platform tools)
if ! command -v adb &> /dev/null; then
	echo "adb not found. Installing..."
	sudo apt install android-sdk-platform-tools -y
fi

# Check and install tcpdump (for network sniffing, if needed)
if ! command -v tcpdump &> /dev/null; then
	echo "tcpdump not found. Installing..."
	sudo apt install tcpdump -y
fi

# Install Python dependencies
pip install -r requirements.txt
