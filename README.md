# PeerTube Uploader

## Requirements
 * python-requests

## Usage
````
$ pip install -r requirements.txt
$ ./peertube-uploader.py 
usage: peertube-uploader.py [-h] [-u USERNAME] [-p PASSWORD] [-c CLIENT_ID]
                            [-s CLIENT_SECRET] [-t ACCESS_TOKEN] -f FILE
                            [-n NAME] [-ch CHANNEL] [-e ENDPOINT] [--private]

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Username
  -p PASSWORD, --password PASSWORD
                        Password
  -c CLIENT_ID, --client_id CLIENT_ID
                        Client ID to use
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        Client secret to use
  -t ACCESS_TOKEN, --access_token ACCESS_TOKEN
                        Access token to use
  -f FILE, --file FILE  File to upload
  -n NAME, --name NAME  Name of the uploaded video
  -ch CHANNEL, --channel CHANNEL
                        Channel ID to upload to
  -e ENDPOINT, --endpoint ENDPOINT
                        Host name
  --private             Set video as private

````
