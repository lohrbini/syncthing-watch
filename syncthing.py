import requests, json, os, time, http.client, urllib

def main():
    while True:
        get_status()
        time.sleep(60)

def get_status():
    r = requests.get('https://' + os.environ['SYNCTHING_URL'] + '/rest/system/connections', headers={'X-API-Key': os.environ['SYNCTHING_API_TOKEN']})
    r_json = r.json()
    system_id = requests.get('https://' + os.environ['SYNCTHING_URL'] + '/rest/system/status', headers={'X-API-Key': os.environ['SYNCTHING_API_TOKEN']})
    system_id_json = system_id.json()
    for conn_id in r_json['connections']:
        if conn_id != system_id_json['myID']:
            if str(r_json['connections']['' + conn_id + '']['connected']) == "True":
                status("200", conn_id)
            else:
                if str(r_json['connections']['' + conn_id + '']['connected']) == "False":
                    status("503", conn_id)
        else:
            print("")

def status(state, identifier):
    conn_id = identifier
    conn_state = state
    if conn_state != "200":
        print(identifier + ' ' + 'not connected')
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": os.environ['PUSHOVER_APP_TOKEN'],
            "user": os.environ['PUSHOVER_USER_TOKEN'],
            "message": str(identifier) + " " + "not connected",
        }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()
        time.sleep(int(os.environ['NOTIFICATION_INTERVAL']))
    else:
        print(identifier + ' ' + 'is connected')
    
if __name__ == "__main__":
    main()
