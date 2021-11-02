#!/usr/bin/env python3
import json
from functions import establish_connection,devices_list

def main():
    url = "https://sandboxdnac2.cisco.com"
    auth = ("devnetuser", "Cisco123!")
    
    token = establish_connection(url,auth)
    devices = devices_list(url,token)
    
    print (json.dumps(devices, indent=2))

    if devices:
        for device in devices:
            print(f'ID: {device["id"]} IP: {device["managementIpAddress"]}')
    else:
        print("error")

if __name__ == '__main__':
    main()
 
