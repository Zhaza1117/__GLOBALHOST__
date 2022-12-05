from socket import timeout
import requests


def _404():
    proxylist = ['58.20.235.180:9091','58.20.232.245:9091','58.20.184.187:9091',
                 '221.4.241.198:9091','112.6.117.135:8085','120.220.220.95:8085',
                 '223.96.90.216:8085','222.65.228.96:8085','106.14.255.124:80',
                 '182.61.201.201:80','85.26.146.169:80','188.254.0.59:80',
                 '91.243.82.126:80','0.0.0.0:9091','0.0.0.0:8085','0.0.0.0:80']

    for question in range(len(proxylist)):
        try:
            req = requests.get('https://google.com', proxies={'http': proxylist[question], 'https': proxylist[question]}, timeout=3)
            print(req.json)
        except:
            print('404 - Server Malfunction')
            pass
