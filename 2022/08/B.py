import sys

mapa = [l[:-1] for l in sys.stdin]

def allless(t,ts):
    return int(t) > max([-1]+[int(c) for c in ts])

def visibility(t,ts):
    r = 0
    for i in range(len(ts)):
        r += 1
        if ts[i] >= t:
            break
    return r

H = len(mapa)
W = len(mapa[0])

def score(y,x):
    l = list(mapa[y][:x])
    l.reverse()
    r = list(mapa[y][x+1:])
    u = [mapa[i][x] for i in range(0,y)]
    u.reverse()
    d = [mapa[i][x] for i in range(y+1,H)]
    c = mapa[y][x]
    v = visibility(c,l)*visibility(c,r)*visibility(c,d)*visibility(c,u)
    return v
    
l = []
for y in range(0,H):
    for x in range(0,W):
        l.append(score(y,x))
print(max(l))

