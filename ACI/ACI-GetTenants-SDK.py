########################################################
# This is an example script that will pull the inventory from an ACI fabric using ACI's REST API and acitoolkit
# leverages devnets ACI sandbox
# Key variables are set in an .env file
########################################################
import json
import os
import sys
from dotenv import load_dotenv
from acitoolkit import acitoolkit
from acitoolkit.acitoolkit import *


load_dotenv()
URL = os.getenv('baseURL')
LOGIN = os.getenv('user')
PASSWORD = os.getenv('pass')

session = acitoolkit.Session(URL, LOGIN, PASSWORD)
resp = session.login()
if resp.status_code != 200:
    print('Could not login to APIC')
    sys.exit(0)

tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)
    print(tenant.descr)
    print('-------------------------------------')
