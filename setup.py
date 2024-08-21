import requests
import json

username = input("Enter your system username: ")
streamer_username = input("Enter the Twitch streamer's username: ")
save_path = input("Enter the desired save path of the output streams (eg. /home/<USER>/mnt/gdrive/recorded_streams/): ")
client_id = input("Enter your Twitch client ID: ")
client_secret = input("Enter your Twitch client secret: ")
url = "https://id.twitch.tv/oauth2/token"
data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
}

response = requests.post(url, data=data)
token_info = response.json()
app_access_token = token_info['access_token']

output = {
    "username": username,
    "client_id": client_id,
    "app_access_token": app_access_token,
    "url": "https://api.twitch.tv/helix/streams",
    "streamer_username": streamer_username,
    "save_path": save_path
}

file_path = 'config.json'

with open(file_path, 'w') as file:
    json.dump(output, file, indent=4)

print("config file created successfully")
