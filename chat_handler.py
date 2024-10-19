def fetch_messages():
	"""Fetch messages from the chat application (placeholder)."""
	# Example messages; replace with actual chat fetching logic
	return ["Message from user1: Let's meet at 192.168.1.1", "Message from user2: Call me at 10.0.0.1"]

def extract_ip_from_message(message):
	"""Extract IP addresses from messages."""
	import re
	ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
	return re.findall(ip_pattern, message)
