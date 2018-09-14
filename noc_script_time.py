#!/usr/bin/python
import requests
import datetime

if __name__ == '__main__':
    API_KEY = raw_input("What is your API key?")
    url = 'https://api.pagerduty.com/incidents'
    headers = {
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'since': datetime.datetime.now()-datetime.timedelta(minutes=200),
        'until': datetime.datetime.now(),
        'service_ids[]': ['P0IL7YX'],
    }
    r = requests.get(url, headers=headers, params=payload)
    print r.json()
