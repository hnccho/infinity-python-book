#!/usr/bin/env python3

o = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10, '十一': 11, '十二': 12, '十三': 13}

for k, v in sorted(o.items(), key=lambda x: x[1]):
    f = '第%s의兒孩%s무섭다고그리오.'
    print(f % (k, '가' if v % 10 == 1 else '도'))
    if v % 10 == 0:
        print()
