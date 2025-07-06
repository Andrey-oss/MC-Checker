'''MC-Checker v1.1'''

# API
#
# https://api.mcsrvstat.us/2/<DOMAIN.TLD>
# https://api.mcsrvstat.us/bedrock/2/<DOMAIN.TLD>

import requests
from core.logo import print_logo
from core.probe_request import probe_request
from core.main import print_srv_info

def main():
    '''Main function cycle'''

    print_logo()
    probe_request()
    server = str(input("Target server: "))
    isbedrock = bool(input("Is this server using the bedrock version? (Y/N): "))

    if isbedrock in ['Y', 'y']:
        r = requests.get("https://api.mcsrvstat.us/bedrock/2/"+server, timeout=5).json()
    else:
        r = requests.get("https://api.mcsrvstat.us/2/"+server, timeout=5).json()

    print_srv_info(r)

if __name__ == '__main__':
    main()
