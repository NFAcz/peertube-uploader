#!/usr/bin/env python
import os
import requests
import argparse
import yaml
from requests_toolbelt.multipart.encoder import MultipartEncoder

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', help='Username', required=True)
parser.add_argument('-p', '--password', help='Password', required=True)
parser.add_argument('-f', '--file', help='File to upload', required=True)
parser.add_argument('-n', '--name', help='Name of the uploaded video')
parser.add_argument('-c', '--channel', help='Channel ID to upload to', default=1)
parser.add_argument('-H', '--host', help='Host name', default='localhost')
parser.add_argument('-P', '--port', help='Port', default=9000)
parser.add_argument('--config', help='Config file', default='config.yml')
parser.add_argument('--private', help='Set video as private', action='store_true')
args = parser.parse_args()

cfg = yaml.load(open(args.config, 'r'))
file_name = os.path.basename(args.file)

auth_url = '/api/v1/users/token'
auth_data = {'client_id': cfg['client_id'],
             'client_secret': cfg['client_secret'],
             'grant_type': 'password',
             'response_type': 'code',
             'username': args.username,
             'password': args.password
             }

upload_url = '/api/v1/videos/upload'
auth_result = requests.post('http://{0}:{1}{2}'.format(args.host, args.port, auth_url), data=auth_data)
access_token = (auth_result.json()['access_token'])

upload_headers = {'Authorization': 'Bearer {0}'.format(access_token)}

session = requests.Session()
with open(args.file, 'rb') as f:
    upload_data = MultipartEncoder({
        'name': file_name,
        'channelId': args.channel,
        'privacy': '2' if args.private else '1',
        'videofile': {"videofile": (file_name, f, "video/mp4")}
        })

    upload_result = session.post('http://{0}:{1}{2}'.format(args.host, args.port, upload_url),
                                  headers=upload_headers,
                                  data=upload_data)
print(upload_result.json())
