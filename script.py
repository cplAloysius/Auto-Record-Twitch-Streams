import requests
import os
import time
from datetime import datetime
import json

with open('config.json', 'r') as f:
	config = json.load(f)

client_id = config.get('client_id')
app_access_token = config.get('app_access_token')
url = config.get('url')
streamer_username = config.get('streamer_username')
save_path = config.get('save_path')

params = {
	"user_login": streamer_username
}

headers = {
	"Authorization": f"Bearer {app_access_token}",
	"Client-ID": client_id
}

print("start checking")

while(True):
	response = requests.get(url, headers=headers, params=params)
	stream_info = response.json()

	if stream_info["data"]:
		timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
		output_file = f"stream_{timestamp}.mp4"
		os.system(f"sudo -u aloysiusloh streamlink --twitch-disable-ads twitch.tv/{streamer_username} best -o '{save_path}{output_file}'")
		continue
	
	time.sleep(60)
