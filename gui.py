from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QComboBox, QMessageBox
from adb_utils import get_connected_devices, open_chat_app
from chat_handler import fetch_messages, extract_ip_from_message

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Code Black Chat Spy")
		self.setGeometry(100, 100, 800, 600)

		self.central_widget = QWidget()
		self.setCentralWidget(self.central_widget)

		self.layout = QVBoxLayout()
		self.central_widget.setLayout(self.layout)

		self.title_label = QLabel("Code Black Chat Spy")
		self.layout.addWidget(self.title_label)

		self.device_combo = QComboBox()
		self.layout.addWidget(self.device_combo)

		self.refresh_devices_button = QPushButton("RefreshDevices")
		self.refresh_devices_button.clicked.connect(self.refresh_devices)
		self.layout.addWidget(self.refresh_devices_button)

		self.open_chat_button = QPushButton("Open Chat App")
		self.open_chat_button.clicked.connect(self.open_chat_app)
		self.layout.addWidget(self.open_chat_button)

		self.chat_area = QTextEdit()
		self.layout.addWidget(self.chat_area)

		self.check_ip_button = QPushButton("Check IP from Chat")
		self.check_ip_button.clicked.connect(self.check_ip)
		self.layout.addWidget(self.check_ip_button)

		self.refresh_devices() # Populate the device list on startup

	def refresh_devices(self):
		"""Refresh the list of connected devices."""
		devices = get_connected_devices()
		self.device_combo.clear()
		self.device_combo.addItems(devices)

	def open_chat_app(self):
		"""Open the chat application."""
		selected_device = self.device_combo.currentText()
		if selected_device:
			app_name = "com.whatsapp/.HomeActivity" # Example for WhatsApp
			open_chat_app(app_name) # Adjust the package name for different apps
			self.chat_area.append(f"Opened chat application on {selected device}.")
		else:
			QMessageBox.warning(self, "Warning", "No device selected!")

	def check_ip(self):
		"""Check for IPs in the messages."""
		messages = fetch_messages() # Placeholder for real message fetching logic
		ips = []
		for message in messages:
		ips.extend(extract_ip_from_message(messages))
		if ips:
			self.chat_area.append(f"Extracted IPs: {','.join(ips)}")
		else:
			self.chat_area.append("No IPs found in messages")
