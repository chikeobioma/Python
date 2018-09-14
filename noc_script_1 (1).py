#!/usr/bin/python
import requests

if __name__ == '__main__':
    API_KEY = raw_input("What is your API key?")
    url = 'https://api.pagerduty.com/incidents'
    headers = {
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'since': '2018-04-10T00:00:00Z',
        'until': '2018-04-11T00:00:00Z',
        'service_ids[]': ['P0IL7YX'],
    }
    r = requests.get(url, headers=headers, params=payload)
    print r.json()
