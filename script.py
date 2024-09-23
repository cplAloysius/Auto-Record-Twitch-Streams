import requests
import os
import subprocess
import time
from datetime import datetime
import json

with open('config.json', 'r') as f:
	config = json.load(f)

my_username = config.get('username')
client_id = config.get('client_id')
app_access_token = config.get('app_access_token')
url = config.get('url')
streamer_username = config.get('streamer_username')
save_path = config.get('save_path')
backup_save = config.get('backup_save')

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
		try:
			subprocess.run(["sudo", "-u", my_username, "streamlink", "--twitch-disable-ads", f"twitch.tv/{streamer_username}", "best", "-o", f"{save_path}{output_file}"], check= True)
		except:
			print("Error writing to path, writing to backup path")
			os.system(f"sudo -u {my_username} streamlink --twitch-disable-ads twitch.tv/{streamer_username} best -o '{backup_save}{output_file}'")
		continue

	time.sleep(60)
