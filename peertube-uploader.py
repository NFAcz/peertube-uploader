#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import requests
import argparse
from mimetypes import guess_type

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', help='Username', default=os.getenv('PEERTUBE_USERNAME', 'user'))
parser.add_argument('-p', '--password', help='Password', default=os.getenv('PEERTUBE_PASSWORD', 'password'))
parser.add_argument('-c', '--client_id', help='Client ID to use', default=os.getenv('PEERTUBE_CLIENT_ID', 'client_id'))
parser.add_argument('-s', '--client_secret', help='Client secret to use', default=os.getenv('PEERTUBE_CLIENT_SECRET', 'client_secret'))
parser.add_argument('-t', '--access_token', help='Access token to use', default=os.getenv('PEERTUBE_ACCESS_TOKEN', 'access_token'))
parser.add_argument('-f', '--file', help='File to upload', required=True)
parser.add_argument('-n', '--name', help='Name of the uploaded video')
parser.add_argument('-ch', '--channel', help='Channel ID to upload to', default=os.getenv('PEERTUBE_CHANNEL_ID', '1'))
parser.add_argument('-e', '--endpoint', help='Host name', default=os.getenv('PEERTUBE_ENDPOINT', 'http://localhost:9000'))
parser.add_argument('--private', help='Set video as private', action='store_true')
args = parser.parse_args()

file_name = os.path.basename(args.file)
file_mime_type = guess_type(args.file)[0]

auth_data = {'client_id': args.client_id,
             'client_secret': args.client_secret,
             'grant_type': 'password',
             'response_type': 'code',
             'username': args.username,
             'password': args.password
             }

upload_data = {'channelId': args.channel,
               'privacy': '2' if args.private else '1',
               'name': args.name if args.name else file_name
               }

if args.access_token is '':
    try:
        auth_result = requests.post('{0}{1}'.format(args.endpoint, '/api/v1/users/token'), data=auth_data)
        access_token = (auth_result.json()['access_token'])
    except:
        print(auth_result.text)
        sys.exit(1)
else:
    access_token = args.access_token 

upload_headers = {'Authorization': 'Bearer {0}'.format(access_token)}

with open(args.file, 'rb') as f:
    upload_result = requests.post('{0}{1}'.format(args.endpoint, '/api/v1/videos/upload'),
                                  headers=upload_headers,
                                  data=upload_data,
                                  files={"videofile": (file_name, f, file_mime_type)})
    try:
        video_uuid = upload_result.json()['video']['uuid']
        print('{0}{1}/{2}'.format(args.endpoint, '/videos/watch', video_uuid))
    except:
        print(upload_result.text)
        sys.exit(1)

