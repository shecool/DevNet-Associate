########################################################
# This is an example script that will pull the inventory from an ACI fabric using ACI's REST API and the requests library
# leverages devnets ACI sandbox
# Key variables are set in an .env file
########################################################
import json
import requests
import os
from dotenv import load_dotenv
import urllib3

#Suppress messages due to self signed cert.]
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 

load_dotenv()


# Set Variables
url = os.getenv('baseURL')
port = os.getenv('port')
user = os.getenv('user')
passw = os.getenv('pass')


# Login to APIC and get token

login_url = f'{url}:{port}/api/aaaLogin.json'
login_body = {
	'aaaUser': {
		'attributes': {
			'name': f'{user}',
			'pwd': f'{passw}'
		}
	}
}

response = requests.post(login_url, data=json.dumps(login_body), verify=False).json()

#Parse token and set cookie
token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-cookie'] = token

# Get fabric nodes
inv_url = f'{url}:{port}/api/node/mo/topology/pod-1.json?query-target=children&target-subtree-class=fabricNode'
response = requests.get(inv_url, cookies=cookie, verify=False).json()

for nodes in response['imdata']:
    print('Device Model: ' + nodes['fabricNode']['attributes']['model'])
    print('Device Serial: ' + nodes['fabricNode']['attributes']['serial'])
    print('Device IP: ' + nodes['fabricNode']['attributes']['address'])
    print('-------------------')