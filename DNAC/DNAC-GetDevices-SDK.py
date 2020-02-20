########################################################
# This is an example script leveraging DNA-Cs Intent API and the DNACenterSDK
# Example script will pull devices on DNAC and output
# Key variables are set in an .env file
########################################################

import json
import requests
import os
from dotenv import load_dotenv
from dnacentersdk import api

# load variables from .env file
load_dotenv()
url = os.getenv('baseURL')
user = os.getenv('user')
passw = os.getenv('pass')

dnac = api.DNACenterAPI(username=user, password=passw, base_url=url)

# Get devices
devices = dnac.devices.get_device_list()
for device in devices['response']:
    print('-----------------------------------------')
    print('Device Type: ' + device['type'])
    print('Device SN: ' + device['serialNumber'])
    print('Device MAC: ' + device['macAddress'])
