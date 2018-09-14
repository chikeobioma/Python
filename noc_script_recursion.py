#!/usr/bin/env python
import requests

def search_all_incidents(myoffset=0):
    url = 'https://api.pagerduty.com/incidents'
    headers = {
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'since': '2018-04-10T00:00:00Z',
        'until': '2018-04-11T00:00:00Z',
        'service_ids[]': ['P0IL7YX'],
        'offset': myoffset,
        'limit': '100'
    }
    r = requests.get(url, headers=headers, data=payload)
    for i in r.json()['incidents']:
        if my_string in i['summary']:
            print i['summary'], i['incident_key']

    if r.json()['more'] is True:
        return search_all_incidents(myoffset + 100)
    
    return None

if __name__ == '__main__':
    API_KEY = raw_input("What is your API key?")
    my_string = raw_input("What string do you want to search for?")
    search_all_incidents()
