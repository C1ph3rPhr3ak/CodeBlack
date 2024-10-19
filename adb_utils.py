# --------------------------------------------------------

# C1ph3rPhr3ak Non-Redistributable License v1.0

# Copyright (c) 2024 C1ph3rPhr3ak. All rights reserved.

# This software is the confidential and proprietary information of C1ph3rPhr3ak. You shall not disclose, distribute, or reproduce such Confidential Information and shall use it only in accordance with the terms of this license.

# DISCLAIMER:
# This software is provided "AS IS," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the author or copyright holder be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

# The author is not liable for any legal actions, damages, or other consequences resulting from the misuse of this software, including but not limited to illegal or malicious use.

# For further inquiries, contact C1ph3rPhr3ak at C1ph3rPhr3ak@proton.me
# ---------------------------------------------------------

import subprocess

def run_adb_command(command):
	"""Run an adb command and return the output."""
	result = subprocess.run(['adb'] + command.split(), capture_output=True, text=True)
	return result.stdout

def get_connected_devices():
	"""Get the list of connected devices."""
	output = run_adb_command('devices')
	devices = []
	for line in output.splitlines()[1:]:
		if line:
			devices.append(line.split()[0]) # Get device ID
	return devices

def open_chat_app(app_name):
	"""Open a chat app on the connected Android device."""
	run_adb_command(f'shell am start -n {app_name}')
