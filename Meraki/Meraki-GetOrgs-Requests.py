############################
# This is an example script that will use the request library to get a list of Meraki organizations
############################
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

url = os.getenv('baseURL')
url = url + '/organizations'
key = os.getenv('API_Key')
headers = {'X-Cisco-Meraki-API-Key': f'{key}',
            'Accept': 'application/json'}

response = requests.get(url, headers=headers).json()
for orgs in response:
    print(orgs['name'] + '-' + orgs['id'])