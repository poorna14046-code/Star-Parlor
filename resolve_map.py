import urllib.request
url = 'https://maps.app.goo.gl/UowkdGo8WKPUc87B9'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=20) as r:
        print('FINAL', r.geturl())
        print('STATUS', r.status)
        print('HEADERS')
        for k, v in r.getheaders():
            print(k+': '+v)
except Exception as e:
    print('ERROR', type(e).__name__, e)
