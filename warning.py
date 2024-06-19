import requests
import os
import sys

from wx import get_wx_data

def get_warning(wx_data, warning_type = "Tornado Warning") -> list:

    features = wx_data['features']
    warning_text = []
    
    for i in features:
        
        if warning_type in i['properties']['headline'] or 'Emergency' in i['properties']['headline']:
            
            warning_string=(i['properties']['headline'] + '\n' + i['properties']['description'])
            warning_text.append(warning_string)

    return warning_text

if __name__ == "__main__":
    os.system('cls')

    url = "https://api.weather.gov/alerts/active?area=" + sys.argv[1].upper()

    if len(sys.argv) >= 3:
        if "tstorm" in sys.argv[2]:
            warning_text = get_warning(get_wx_data(url), "Thunderstorm Warning")
    else:
        warning_text = get_warning(get_wx_data(url))
    for i in warning_text:
        print (i)
        input('Press Enter to continue.')
        os.system('cls')
