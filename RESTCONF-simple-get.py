import json
import requests
from pprint import pprint

# dictionary about the router
router = {"host": "10.0.20.55", "port": "443", "username": "VandersonKjdy7s3y", "password": "&SBJEwkwis98f7u&2"}

# dictionary about the HTTP headers
headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

response = requests.get(url, headers=headers, auth=(
 router['username'], router["password"]), verify=False)

api_data = response.json()
print("/" * 50)
pprint(api_data["Cisco-IOS-XE-interfaces-oper:interfaces/interface"]["description"])
print("/" * 50)
if api_data["Cisco-IOS-XE-interfaces-oper:interfaces/interface"]["admin-status"] == 'if-state-up':
 print("Interface is UP")





