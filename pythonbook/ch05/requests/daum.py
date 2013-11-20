import requests

url = "http://apis.daum.net/search/board"
p = {'q': '아이유',
     'result': '2',
     'pageno': '1',
     'output': 'json',
     'apikey': 'DAUM_SEARCH_DEMO_APIKEY'}

print('Requesting %s ...\n' % url)
r = requests.get(url, params=p)

print(r.text)
