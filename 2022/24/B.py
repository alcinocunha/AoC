import sys

mapa = {}
for (y,l) in enumerate(list(sys.stdin)[1:-1]):
    mapa[y] = {}
    for (x,c) in enumerate(l[1:-2]):
        if c in "><v^":
            mapa[y][x] = c
        else:
            mapa[y][x] = '.'
Y = y+1
X = x+1
mapa[-1] = {0:'.'}
mapa[Y] = {X-1:'.'}

def occupied(i,x,y):
    return (x,y) != (0,-1) and (x,y) != (X-1,Y) and (mapa[(y-i) % Y][x] == 'v' or mapa[(y+i) % Y][x] == '^' or mapa[y][(x-i)%X] == '>' or mapa[y][(x+i)%X] == '<')

def vis(i,x,y):
    return [(x,y) for (x,y) in [(x,y),(x+1,y),(x-1,y),(x,y-1),(x,y+1)] if y in mapa and x in mapa[y] and not occupied(i,x,y)]

dist = {(0,-1)}
i = 0
while (X-1,Y) not in dist:
    i += 1
    new = set()
    for p in dist:
        new.update(vis(i,*p))
    dist = new
dist = {(X-1,Y)}
while (0,-1) not in dist:
    i += 1
    new = set()
    for p in dist:
        new.update(vis(i,*p))
    dist = new
dist = {(0,-1)}
while (X-1,Y) not in dist:
    i += 1
    new = set()
    for p in dist:
        new.update(vis(i,*p))
    dist = new

print(i)
