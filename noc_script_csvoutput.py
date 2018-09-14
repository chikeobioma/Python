#!/usr/bin/python
import requests
import csv

if __name__ == '__main__':
    API_KEY = raw_input("What is your API key?")
    url = 'https://api.pagerduty.com/incidents?time_zone=UTC&include%5B%5D=first_trigger_log_entries'
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
    OUTPUT_FILE = './output.csv'
    fileobject = open(OUTPUT_FILE, 'w')
    writer = csv.writer(fileobject)
    writer.writerow(['Title', 'Escalation Policy', 'Service'])
    for i in r.json()['incidents']:
        try:
            writer.writerow([i['summary'], i['escalation_policy']['summary'], i['first_trigger_log_entry']['channel']['service']])
        except KeyError:
            writer.writerow([i['summary'], i['escalation_policy']['summary'], "None"])
    fileobject.close()
