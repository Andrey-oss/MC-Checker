import sys

def server_chk(debug_info):
    if debug_info['ping'] == False:
       print ("")
       print ("[-] Server doesn't exist or server host is down!")
       sys.exit()
