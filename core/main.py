'''Module which retrives information about the server'''

import json

def print_srv_info(r: dict):
    '''Print server information'''

    try:
        data = json.loads(json.dumps(r))

        debug_info = data.get('debug', {})
        if not debug_info:
            exit("[-] Server doesn't exist or server host is down!")

        motd_info = data.get('motd', {})
        players_info = data.get('players', {})

        print("")

        # Basic info
        if 'online' in data:
            print(f"[+] Server online: {data['online']}")
        if 'ip' in data:
            print(f"[+] Server IP: {data['ip']}")
        if 'hostname' in data:
            print(f"[+] Server hostname: {data['hostname']}")
        if 'port' in data:
            print(f"[+] Server port: {data['port']}")

        # MOTD info
        clean_motd = motd_info.get('clean', [])
        if clean_motd:
            motd_text = clean_motd[0].lstrip()
            print(f"[+] MOTD: {motd_text}")

        if 'animatedmotd' in debug_info:
            print(f"[+] Animated MOTD: {debug_info['animatedmotd']}")

        # Players info
        if 'online' in players_info:
            print(f"[+] Players now: {players_info['online']}")
        if 'max' in players_info:
            print(f"[+] Max players allowed: {players_info['max']}")

        # Version info
        if 'version' in data:
            print(f"[+] Server versions: {data['version']}")

    except Exception as e:
        print(f"[!] Error processing server info: {e}")
