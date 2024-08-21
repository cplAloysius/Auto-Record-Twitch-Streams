# Record Twitch Streams

## A Python script to record and save Twitch streams for viewing at a later time.

I created this project as I was constantly missing streams from a streamer whenever they went live. Since the streamer did not have Video On Demand (VODs) enabled, I could not watch the stream after it ended. I set up the script to run on startup as a systemd service on a Raspberry Pi 3, and save the output stream to a cloud storage service (Google Drive), mounted on my Rpi with [rclone](https://github.com/rclone/rclone).

The script uses the Twitch API [Get Streams](https://dev.twitch.tv/docs/api/reference/#get-streams) endpoint to periodically check if the specified streamer is live.
If they are, it then uses [Streamlink](https://github.com/streamlink/streamlink) to record the stream and save it into an output file.

## How to install

1. Log in to the [Twitch Developer Console](https://dev.twitch.tv/console) to register a new application and obtain your client ID and client secret.
2. Clone this repository on the desired machine that you will be running the script on, and `cd` into it.
3. `python setup.py`, which creates a config.json file containing the following information:
    * Your system username
    * Desired streamer's Twitch username
    * Location to save the output stream file (format: /xxx/yyy/zzz/)
    * Client ID you obtained from registering a new application on the Twitch Developer Console
    * Client Secret
4. `python script.py` to start the script

## How to run the script on startup (Rpi)

1. Create a systemd service and give it a name: `sudo nano /lib/systemd/system/<SERVICE_NAME>.service`
```
[Unit]
Description=Record Twitch streams
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python /PATH/TO/CLONED/REPO/script.py
WorkingDirectory=/PATH/TO/CLONED/REPO
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```
* `Restart=always` ensures that the service is always active and restarts if it is stopped or cancelled (unless stopped by `sudo systemctl stop <SERVICE_NAME>
* `RestartSec=10` overcomes the maximum limit of 5 restart attempts in 10 seconds

2. Enable and start the service
```
sudo systemctl enable <SERVICE_NAME>
sudo systemctl start <SERVICE_NAME>
```
3. To disable the service: `sudo systemctl disable <SERVICE_NAME>`

## Saving output file on mounted cloud service


Saving the output stream file onto a cloud storage service means not having to `scp` each file from the Rpi to my computer to watch the recording, which could take hours due to the size of the files.

This [Medium article](https://medium.com/@artur.klauser/mounting-google-drive-on-raspberry-pi-dd15193d8138) by [Artur Klauser](https://github.com/ArturKlauser) covers how to mount Google Drive (or most other cloud storage services) onto your Rpi on startup.
Once this is done, the recorded stream will be saved onto your Google Drive and can be streamed directly from Google Drive, or downloaded for offline viewing.
