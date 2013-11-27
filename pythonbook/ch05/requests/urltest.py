#!/usr/bin/env python

import re, sys

import requests

f = open(sys.argv[1], encoding='utf-8')
text = f.read()
for url in re.findall('http[s]?://[a-zA-Z0-9_:/%$?=\.\-\+]*', text):
    try:
        r = requests.request('GET', url)
        status = str(r.status_code)
    except:
        status = 'N/A'
    print('%s %s' % (status, url))
