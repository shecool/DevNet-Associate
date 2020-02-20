###########################################################
# This is an exaple script which leverages the Meraki Dashboard API using the Python SDK
# Print all devices under each Network in an Org
# API Key and other variables kept in a seperate .env file
###########################################################
import os
from dotenv import load_dotenv
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from meraki_sdk.exceptions.api_exception import APIException

load_dotenv()

x_cisco_meraki_api_key = os.getenv("API_Key")
meraki = MerakiSdkClient(x_cisco_meraki_api_key)


params = {}
params["organization_id"] = os.getenv("org_Id")
nets = meraki.networks.get_organization_networks(params)

for network in nets:
    print(f'########## {network["name"]} ##########')
    devices = meraki.devices.get_network_devices(network["id"])
    for device in devices:
        print(f'{device["model"]}        SN: {device["serial"]}')
