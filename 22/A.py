import sys

Y = 0
X = 0
mapa = {}
l = sys.stdin.readline()
y = 0
while l != "\n":
    mapa[y] = {}
    for x in range(len(l[:-1])):
        if l[x] != ' ':
            mapa[y][x] = l[x]
    X = max(x+1,X)
    y += 1
    l = sys.stdin.readline()
Y = y
y = 0
d = 0
x = min(mapa[0].keys())

cs = sys.stdin.readline()[:-1]

def next(x,y,d):
    if d == 0:
        return (x+1,y)
    if d == 1:
        return (x,y+1)
    if d == 2:
        return (x-1,y)
    if d == 3:
        return (x,y-1)

c = 0
while c < len(cs):
    if cs[c] == 'R':
        d = (d+1)%4
    elif cs[c] == 'L':
        d = (d-1)%4
    else:
        e = c
        while (e < len(cs) and cs[e] != 'R' and cs[e] != 'L'):
            e += 1
        n = int(cs[c:e])
        for i in range(n):
            nx,ny = next(x,y,d)
            nx = nx % X
            ny = ny % Y
            if nx not in mapa[ny]:
                while nx not in mapa[ny]:
                    nx,ny = next(nx,ny,d)
                    nx = nx % X
                    ny = ny % Y
            if mapa[ny][nx] == '#':
                break
            else:
                x,y = nx,ny
    c += 1

print((x+1)*4+(y+1)*1000+d)
