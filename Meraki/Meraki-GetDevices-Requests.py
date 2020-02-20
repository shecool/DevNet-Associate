###########################################################
# This is an exaple script which leverages the Meraki Dashboard API using requests
# Print all devices under each Network in an Org
# API Key and other variables kept in a seperate .env file
###########################################################

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('baseURL')
key = os.getenv('API_Key')
org_Id = os.getenv('org_Id')
networks_url = f'{url}/organizations/{org_Id}/networks'
headers = {'X-Cisco-Meraki-API-Key': f'{key}', 
            'Accept': 'application/json'}

response = requests.get(networks_url, headers=headers).json()

for networks in response:
    print(f'######### {networks["name"]} #########')
    devices_url = f'{url}/networks/{networks["id"]}/devices'
    devices_response = requests.get(devices_url,headers=headers).json()
    for devices in devices_response:
        print(f'{devices["model"]}     SN: {devices["serial"]}')
