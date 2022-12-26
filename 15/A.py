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

y = 2000000
r = 0
for x in range(minX,maxX+1):
    if (x,y) in beacon:
        continue
    for (sx,sy) in radius:
        if abs(sx-x) + abs(sy-y) <= radius[(sx,sy)]:
            r += 1
            break

print(r)
