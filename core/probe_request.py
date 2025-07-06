'''Check for internet connection'''

import requests

def probe_request():
    '''Do probe request'''

    try:
        requests.get("https://github.com", timeout=5)
    except requests.exceptions.RequestException:
        exit("[-] Tool cannot be started due to internet connection!")
