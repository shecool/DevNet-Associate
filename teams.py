import requests
import json
##########
## I've made changes locally
# Get your token here after logging in: https://developer.webex.com/docs/api/getting-started
token = 'MTVjOTQzNGUtZjkyZS00OTgxLTk5MmYtNDRkMDU5NzVjYTczMDBmMjVlNTMtOGY0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'

### Create a Team ###
url = 'https://api.ciscospark.com/v1/teams'
headers = {'Authorization': f'Bearer {token}',
           'Content-Type': 'application/json'}

body = {
    "name": "CBT Team"
}

# post_response = requests.post(
#     url, headers=headers, data=json.dumps(body)).json()
# print(post_response)


get_response = requests.get(url, headers=headers).json()
#teamId = get_response['items'][0]['id']
teams = get_response['items']
# print(teams[0]['name'])
for team in teams:
    if team['name'] == 'CBT Team':
        teamId = team['id']
        print(teamId)

###### CREATE A ROOM #######
room_url = 'https://api.ciscospark.com/v1/rooms'
room_body = {
    "title": "CBT Room",
    "teamId": teamId
}
##This is the trying branch##

room_post = requests.post(room_url, headers=headers, data=json.dumps(room_body)).json()

get_rooms = requests.get(room_url, headers=headers).json()
rooms = get_rooms['items']
for room in rooms:
    if room['title'] == 'CBT Room':
        roomId = room['id']

#### POST A MESSAGE TO THE ROOM ######
msg_url = 'https://api.ciscospark.com/v1/messages'
msg_body = {
    "roomId": roomId,
    'text': 'ALERT: Interface on device XYZ is down'
}

msg_response = requests.post(
    msg_url, headers=headers, data=json.dumps(msg_body)).json()