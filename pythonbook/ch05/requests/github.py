#!python3

import requests

url = 'https://api.github.com/user'
print('Requesting to %s ...\n' % url)
r = requests.get(url, auth=('user', 'pass'))

print('r.status_code: %d' % r.status_code)
print('r.headers[\'content-type\']: %s' % r.headers['content-type'])
print('r.encoding: %s' % r.encoding)
print('type(r.text): %s' % type(r.text))
print('type(r.json()): %s' % type(r.json()))
