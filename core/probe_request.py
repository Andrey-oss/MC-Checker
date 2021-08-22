import requests
import sys

def probe_request():
    try:
       requests.get("https://github.com", timeout=5)
    except Exception:
       print ("[-] Tool cannot be started due to internet connection!")
       sys.exit()
