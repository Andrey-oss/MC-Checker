import json
from core.server_checker import server_chk

def main(r):
    basic = json.dumps(r)
    basic_info = json.loads(basic)
    debug = json.dumps(basic_info['debug'])
    debug_info = json.loads(debug)
    server_chk(debug_info)
    motd = json.dumps(basic_info['motd'])
    motd_info = json.loads(motd)
    players = json.dumps(basic_info['players'])
    players_info = json.loads(players)
    print ("")
    try:
       server_online = basic_info['online']
    except Exception:
       pass
    else:
       print ("[+] Server online: "+str(server_online))
    try:
       ip = basic_info['ip']
    except Exception:
       pass
    else:
       print ("[+] Server IP: "+ip)
    try:
       hostname = basic_info['hostname']
    except Exception:
       pass
    else:
       print ("[+] Server hostname: "+hostname)
    try:
      port = basic_info['port']
    except Exception:
       pass
    else:
       print ("[+] Server port: "+str(port))
    try:
       clean_motd = motd_info['clean']
    except Exception:
       pass
    else:
       try:
          motd_text = clean_motd[0]
       except Exception:
          pass
       else:
          print ("[+] MOTD: "+motd_text.lstrip())
    try:
       animated_motd = debug_info['animatedmotd']
    except Exception:
       pass
    else:
        print ("[+] Animated MOTD: "+str(animated_motd))
    try:
       players_online = players_info['online']
    except Exception:
       pass
    else:
       print ("[+] Players now: "+str(players_online))
    try:
       players_max = players_info['max']
    except Exception:
       pass
    else:
       print ("[+] Max players allowed: "+str(players_max))
    try:
       server_versions = basic_info['version']
    except Exception:
       pass
    else:
       print ("[+] Server versions: "+server_versions)
