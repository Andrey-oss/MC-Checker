# API
#
# https://api.mcsrvstat.us/2/<DOMAIN.TLD>
# https://api.mcsrvstat.us/bedrock/2/<DOMAIN.TLD>

import requests
import sys
import os
import json
from core.logo import print_logo
from core.probe_request import probe_request
from core.main import main

print_logo()
probe_request()
server = input("Target server: ")
r = requests.get("https://api.mcsrvstat.us/2/"+server).json()
main(r)
