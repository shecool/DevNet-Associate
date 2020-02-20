########################################################
# This is an example script leveraging Cisco SD-WAN's vManage APIs and the requests library
# Example script will pull devices in vManage and output
# Key variables are set in an .env file
########################################################

import requests
import json
import os
from dotenv import load_dotenv
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # Disables annoying unverifed HTTPS message

load_dotenv()
url = os.getenv('baseURL')
user = os.getenv('user')
passw = os.getenv('pass')
port = os.getenv('port')

url = url + ':' + port

login_body = {'j_username': f'{user}',
            'j_password': f'{passw}'}

# create session
login_url = url + '/j_security_check'
session = requests.session()
response = session.post(login_url, data=login_body, verify=False)

# We will get an error 200 regardless of failure or success
# If the body is empty, this means a successful login.
# If the login failed, typically it will send an HTML page
if response.text:
    print('########### Login failed ############')
    import sys
    sys.exit(1)
else:
    print('############ Login Successful! ############')

device_url = url + '/dataservice/device'
d_response = session.get(device_url, verify=False).json()
print('############ Devices ############')
for devices in d_response['data']:
    print('Device ID: ' +devices['deviceId'])
    print('IP address: ' +devices['system-ip'])
    print('Hostname: ' +devices['host-name'])
    print('Stats: ' +devices['status'])
    print('-------------------------------------')
