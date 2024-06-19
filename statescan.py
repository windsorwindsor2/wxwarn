import requests
import threading
import sys

from wx import get_wx_data

states = ['AL',
'AK',
'AZ',
'AR',
'CA',
'CO',
'CT',
'DE',
'FL',
'GA',
'HI',
'ID',
'IL',
'IN',
'IA',
'KS',
'KY',
'LA',
'ME',
'MD',
'MA',
'MI',
'MN',
'MS',
'MO',
'MT',
'NE',
'NV',
'NH',
'NJ',
'NM',
'NY',
'NC',
'ND',
'OH',
'OK',
'OR',
'PA',
'RI',
'SC',
'SD',
'TN',
'TX',
'UT',
'VT',
'VA',
'WA',
'WV',
'WI',
'WY']




url_start = "https://api.weather.gov/alerts/active?area="
alert_states = []
threads = []

def check_state(state, warning_type = "Tornado Warning"):
    print(f"Requesting {state}")
    url = url_start + state
    alert = get_wx_data(url)
    features = alert['features']
    try:
        for i in features:
            if warning_type in i['properties']['headline']:
                alert_states.append(state)
    except:
        print(f"No warnings in {state}")

if len(sys.argv) >= 2:
    if "tstorm" in sys.argv[1]:
        warning_type = "Thunderstorm Warning"
else:
    warning_type = "Tornado Warning"

for state in states:
    thread = threading.Thread(target=check_state, args=(state, warning_type))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(alert_states)