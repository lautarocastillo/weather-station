import requests

class MyIp:
    def get():
        url = "https://api.duckduckgo.com/?q=my+ip&format=json&no_html=1&skip_disambig=1"
        r   = requests.get(url)
        ip  = r.json()['Answer']
        return ip
