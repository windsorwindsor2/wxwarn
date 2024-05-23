import requests
import os

os.system('cls')

url = "https://api.weather.gov/alerts/active?area=OK"

def get_wx_data(url):
    response = requests.get(url)
    return response.json()

'''
keys:
'@context'
'type'
features = Bulk of data
'title' - Title of requested data
'updated'
'''
def printmeta(alert):
    keys = ['@context', 'type', 'title', 'updated']
    for key in keys:
        print (alert[key])

def printkeys(alert):
    for i in alert:
        print (i)
alert = get_wx_data(url)

features = alert['features']

'''
keys:
headline
data
description
'''
for i in features:
    if 'Tornado Warning' in i['properties']['headline']:
        print(i['properties']['headline'])
        print(i['properties']['description'])
        input('Press Enter to continue.')
        os.system('cls')
