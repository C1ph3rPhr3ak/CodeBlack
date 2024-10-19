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
