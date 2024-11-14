#!/usr/bin/env python3

''' ISS Challenge | Jonathan Johnny'''
import reverse_geocoder as rg
import requests
from datetime import datetime

API='http://api.open-notify.org/iss-now.json'

def main():
    resp = requests.get(API).json()
    print(f'Current position of ISS at {datetime.fromtimestamp(resp["timestamp"])}')
    print(f'Latitude: {resp["iss_position"]["latitude"]}')
    print(f"Longitude: {resp['iss_position']['longitude']}")
    location =(resp["iss_position"]["latitude"] , resp['iss_position']['longitude'])
    place = rg.search(location, verbose = False)[0]
    print(f'City/Country: {place["name"]}, {place["cc"]}')

if __name__ == "__main__":
    main()
