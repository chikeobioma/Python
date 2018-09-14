#!/usr/bin/python
import requests

if __name__ == '__main__':
    API_KEY = raw_input("What is your API key?")
    url = 'https://api.pagerduty.com/incidents'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'since': '2018-04-10T00:00:00Z',
        'until': '2018-04-11T00:00:00Z',
        'service_ids[]': ['P0IL7YX'],
    }
    r = requests.get(url, headers=headers, params=payload)
    my_string = raw_input("Input a string to match against")
    for i in r.json()['incidents']:
        if my_string in i['summary']:
            print i['summary'], i['incident_key']
