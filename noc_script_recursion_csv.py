#!/usr/bin/env python
import requests
import csv
import datetime

def csv_start():
    """
    Create header fields for csv file.
    """
    fileobject = open(OUTPUT_FILE, 'w')
    writer = csv.writer(fileobject)
    writer.writerow(['Summary','HTML URL'])
    fileobject.close()

def csv_add_incident_array(csv_line_array):
    """
    Add array to csv file.
    """
    fileobject = open(OUTPUT_FILE, 'a')
    writer = csv.writer(fileobject)
    for csv_line in csv_line_array:
        writer.writerow(csv_line)
    fileobject.close()

def search_all_incidents(myoffset=0):
    url = 'https://api.pagerduty.com/incidents'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'since': '2018-04-10T00:00:00Z',
        'until': '2018-04-11T00:00:00Z',
        'service_ids[]': ['P0IL7YX'],
        'limit': 100,
        'offset': myoffset
    }
    r = requests.get(url, headers=headers, data=payload)
    print("we are on offset ", myoffset)
    mylist=[]
    for incident in r.json()['incidents']:
        if my_string in incident['summary']:
            mylist.append([incident['summary'], incident['html_url']])

    csv_add_incident_array(mylist)

    if r.json()['more'] == True:
        return search_all_incidents(myoffset + 100)
    else:
        return None
    return None

if __name__ == '__main__':
    API_KEY = raw_input("What is your API key?")
    my_string = raw_input("What string do you want to search for?")
    OUTPUT_FILE = "./output" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
    csv_start()
    search_all_incidents()
