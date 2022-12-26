import sys

mapa = [l[:-1] for l in sys.stdin]

def allless(t,ts):
    return int(t) > max([-1]+[int(c) for c in ts])

H = len(mapa)
W = len(mapa[0])

def visible(y,x):
    l = mapa[y][:x]
    r = mapa[y][x+1:]
    u = [mapa[i][x] for i in range(0,y)]
    d = [mapa[i][x] for i in range(y+1,H)]
    c = mapa[y][x]
    return allless(c,l) or allless(c,r) or allless(c,u) or allless(c,d)

v = 0
for y in range(0,H):
    for x in range(0,W):
        if visible(y,x):
            v += 1
print(v)

