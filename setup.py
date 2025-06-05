import requests
import json
import os

old_path = "config.json"

if os.path.exists(old_path):
    with open(old_path, 'r') as f:
        config = json.load(f)
else:
    config = {}

def prompt_input(prompt_text, key):
    while True:
        value = input(prompt_text)
        if value:
            return value
        elif key in config:
            print(f"Using saved value for '{key}': {config[key]}")
            return config[key]
        else:
            print(f"No previous value found for '{key}'. Please enter a value.")


username = prompt_input("Enter your system username: ", "username")
streamer_username = prompt_input("Enter the Twitch streamer's username: ", "streamer_username")
save_path = prompt_input("Enter the desired save path of the output streams (eg. /home/<USER>/mnt/gdrive/recorded_streams/): ", "save_path")
backup_save =  prompt_input("Enter a backup save path (will write output stream here only if writing to save_path fails): ", "backup_save")
client_id = prompt_input("Enter your Twitch client ID: ", "client_id")
client_secret = prompt_input("Enter your Twitch client secret: ", "client_secret")
tel_token = prompt_input("Enter your telegram bot token: ", "tel_token")
tel_chat_id = prompt_input("Enter your telegram chat id: ", "tel_chat_id")

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
    "save_path": save_path,
    "backup_save": backup_save,
    "tel_token": tel_token,
    "tel_chat_id": tel_chat_id,
}

file_path = 'config.json'

with open(file_path, 'w') as file:
    json.dump(output, file, indent=4)

print("config file created successfully")
