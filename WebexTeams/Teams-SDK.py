########################################################
# This is an example script Webex Teams REST API and requests library
# Example script will create a space, add members, and post a message
# Key variables are set in an .env file
########################################################

import json
import os
from dotenv import load_dotenv
from webexteamssdk import WebexTeamsAPI

load_dotenv()
token = os.getenv('token')
url = os.getenv('baseURL')
email=os.getenv('email')

webex = WebexTeamsAPI(access_token=token)

# Create room
room = webex.rooms.create("Webexsdk test room")

# Add person
webex.memberships.create(roomId=room.id, personEmail=email)

# Post Message
webex.messages.create(roomId=room.id, text="Hello world!")