#!/usr/bin/env python3

from itertools import cycle

c = cycle('四角形의內部의')
s = ''
for i in range(31):
    s = s + next(c)

print(s)
