#!/usr/bin/python
import requests

if __name__ == '__main__':
    API_KEY = raw_input("What is your API key?")
    url = 'https://api.pagerduty.com/incidents'
    headers = {'Authorization': 'Token token={token}'.format(token=API_KEY)}
    payload = {}
    print requests.get(url, headers=headers, params=payload).json()
