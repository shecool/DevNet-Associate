########################################################
# This is an example script Webex Teams REST API and requests library
# Example script will create a space, add members, and post a message
# Key variables are set in an .env file
########################################################

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')
url = os.getenv('baseURL')
email=os.getenv('email')
headers = {'Authorization': f'Bearer {token}'}

# Create a new teams room
rooms_body = {'title': 'DevNet Practice for SY'}
rooms_url = url + '/rooms'
response = requests.post(rooms_url, headers=headers, data=rooms_body).json()
room_id = response['id']

# Add someone to the room based on email
mem_url = url + '/memberships'
mem_body = {'roomId': f'{room_id}',
            'personEmail': f'{email}'}
response = requests.post(mem_url, headers=headers, data=mem_body)
if response.status_code == 200:
    print(f'######## {email} added to space ######')
else:
    print('######### Something went wrong. ########')

# Post a Message to the room
message_url = url + '/messages'
message_body = {'roomId': f'{room_id}',
                'text': 'Hello world!'}
response = requests.post(message_url, headers=headers, data=message_body)
if response.status_code == 200:
    print('######## Message posted! ######')
else:
    print('######### Something went wrong. ########')

