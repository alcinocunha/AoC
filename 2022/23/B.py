import sys

def vis(x,y):
    return [(x+1,y),(x+1,y+1),(x+1,y-1),(x,y-1),(x,y+1),(x-1,y),(x-1,y+1),(x-1,y-1)]

def round(n,x,y):
    if n == 0:
        return [(x,y-1),(x-1,y-1),(x+1,y-1)]
    if n == 1:
        return [(x,y+1),(x-1,y+1),(x+1,y+1)]
    if n == 2:
        return [(x-1,y),(x-1,y-1),(x-1,y+1)]
    if n == 3:
        return [(x+1,y),(x+1,y-1),(x+1,y+1)]

def move(n,x,y):
    return round(n,x,y)[0]

mapa = set()
for y,l in enumerate(sys.stdin):
    for x in range(len(l[:-1])):
        if l[x] == '#':
            mapa.add((x,y))

i = 0
old = set()
while mapa != old:
    new = {}
    same = set()
    for e in mapa:
        if all([p not in mapa for p in vis(*e)]):
            same.add(e)
            continue
        for n in range(0,4):
            if all([p not in mapa for p in round((n+i)%4,*e)]):
                p = move((n+i)%4,*e)
                for d in new:
                    if new[d] == p:
                        same.add(e)
                        same.add(d)
                        break
                new[e] = p
                break
        else:
            same.add(e)
    old = set(mapa)
    mapa = set()
    for e in old:
        if e not in same:
            mapa.add(new[e])
        else:
            mapa.add(e)
    i += 1

print(i)
