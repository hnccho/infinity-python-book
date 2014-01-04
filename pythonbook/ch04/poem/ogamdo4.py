l = list('.0987654321')

for i in range(len(l)):
    print(' '.join(l))
    d = l.index('.')
    if d + 1 < len(l):
        l[d], l[d+1] = l[d+1], l[d]
