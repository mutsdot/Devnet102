#! /usr/bin/env python
from dnacentersdk import api

DNAC = api.DNACenterAPI(username = "devnetuser",
    password = "Cisco123!",
    base_url = "https://sandboxdnac2.cisco.com")

DEVICES = DNAC.devices.get_device_list()

print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format("Device Name", "|", "Device Type", "|", "Up time"))
print("-"*95)

for DEVICE in DEVICES.response:
     print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format(DEVICE.hostname, "|", DEVICE.type, "|", DEVICE.upTime))

print("-"*95)
