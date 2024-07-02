import requests
import os

'''
pass a URL ot the function of the following format:
https://api.weather.gov/alerts/active?area=OK
Replace "OK" with any two-letter state abbreviation
'''
 
def get_wx_data(url):
    response = requests.get(url)
    return response.json()

def state_url(state):
    if len (state) != 2:
        raise RuntimeError ("Use a valid 2-letter state abbreviation")
    url = "https://api.weather.gov/alerts/active?area=" + state

    return url


def printmeta(alert):
    keys = ['@context', 'type', 'title', 'updated']
    for key in keys:
        print (alert[key])

def printkeys(alert):
    for i in alert:
        print (i)

'''
keys:
'@context'
'type'
features = Bulk of data
'title' - Title of requested data
'updated'

keys in features:
headline
data
description
'''

if __name__ == "__main__":
    #Use Oklahoma as an example because tornados.
    url = "https://api.weather.gov/alerts/active?area=OK"
    
    alert = get_wx_data(url)

    features = alert['features']

    os.system('cls')

    for i in features:
        if 'Tornado Warning' in i['properties']['headline']:
            print(i['properties']['headline'])
            print(i['properties']['description'])
            input('Press Enter to continue.')
            os.system('cls')
