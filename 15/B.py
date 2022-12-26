import sys

beacon = set()
radius = {}

minX = float('inf')
maxX = -float('inf')

for l in sys.stdin:
    _,a,b,c,d = l.split('=')
    sx = int(a.split(',')[0])
    sy = int(b.split(':')[0])
    bx = int(c.split(',')[0])
    by = int(d)
    beacon.add((bx,by))
    r = abs(sx-bx) + abs(sy-by)
    radius[(sx,sy)] = r
    minX = min(minX,sx-r)
    maxX = max(maxX,sx+r)

M = 4000000
for x in range(0,M+1):
    y = 0
    while y <= M:
        for (sx,sy) in radius:
            d = abs(sx-x) + abs(sy-y)
            if d <= radius[(sx,sy)]:
                y = sy + radius[(sx,sy)] - abs(sx-x) + 1
                break
        else:
            print(x*M+y)
            exit()
