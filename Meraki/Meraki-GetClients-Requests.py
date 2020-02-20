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
    clients_url = f'{url}/networks/{networks["id"]}/clients'
    clients_response = requests.get(clients_url,headers=headers).json()
    for clients in clients_response:
        print(f'{clients["description"]}     MAC: {clients["mac"]}')
