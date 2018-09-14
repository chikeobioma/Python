#!/usr/bin/env python
import requests
import csv
import datetime

if __name__ == '__main__':
    API_KEY = raw_input("What is your API key?")
    my_string = raw_input("What string do you want to search for?")
    more = True
    myoffset = 0
    OUTPUT_FILE = "./output" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
    fileobject = open(OUTPUT_FILE, 'w')
    writer = csv.writer(fileobject)
    writer.writerow(['Title', 'Escalation Policy', 'Service'])
    while more == True:
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
                try:
                    writer.writerow([i['summary'], i['escalation_policy']['summary'], i['first_trigger_log_entry']['channel']['service']])
                except KeyError:
                    writer.writerow([i['summary'], i['escalation_policy']['summary'], "None"])

        more = r.json()['more']
        myoffset = myoffset + 100
    fileobject.close()
