#!/usr/bin/pythin python3
import requests

def establish_connection(url,auth):
    path = "/dna/system/api/v1/auth/token"
    headers = {
        "Content-Type": "application/json"
    }
    session = requests.post(
        f'{url}{path}',auth=auth,headers=headers
    )
    session.raise_for_status()
    token = (session.json()["Token"])
    return token

def devices_list(url,token):

    path = "/dna/intent/api/v1/network-device"
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token
    }
    session = requests.get(
        f'{url}{path}',headers=headers
    )
    session.raise_for_status()
    return session.json()["response"]
