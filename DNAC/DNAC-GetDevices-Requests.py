########################################################
# This is an example script leveraging DNA-Cs Intent API and the requests library
# Example script will pull devices on DNAC and output
# Key variables are set in an .env file
########################################################
import json
import requests
import os
from dotenv import load_dotenv

# load variables from .env file
load_dotenv()
url = os.getenv('baseURL')
user = os.getenv('user')
passw = os.getenv('pass')

# Login to DNAC and get a token
login_url = url + '/dna/system/api/v1/auth/token'
response = requests.post(login_url, auth=(user,passw)).json()
token = response['Token']
# Set the token in the header
headers = {'X-auth-token': f'{token}'}

# Get Network devices from DNAc
print('DNA Center Device Inventory')
devices_url = url + '/dna/intent/api/v1/network-device'
response = requests.get(devices_url, headers=headers).json()
for devices in response['response']:
    print('-----------------------------------------')
    print('Device Type: ' + devices['type'])
    print('Device SN: ' + devices['serialNumber'])
    print('Device MAC: ' + devices['macAddress'])