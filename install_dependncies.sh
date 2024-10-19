# ---------------------------------------------------

# C1ph3rPhr3ak Non-Redistributable License v1.0

# Copyright (c) 2024 C1ph3rPhr3ak. All rights reserved.

# This software is the confidential and proprietary information of C1ph3rPhr3ak. You shall not disclose, distribute, or reproduce such Confidential Information and shall use it only in accordance with the terms of this license.

# DISCLAIMER:
# This software is provided "AS IS," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the author or copyright holder be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

# The author is not liable for any legal actions, damages, or other consequences resulting from the misuse of this software, including but not limited to illegal or malicious use.

# For further inquiries, contact C1ph3rPhr3ak at C1ph3rPhr3ak@proton.me
# ----------------------------------------------------

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
