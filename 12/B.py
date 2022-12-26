import sys

mapa = {}

def succ(c):
    return chr(ord(c)+1)

def bfs(o,X,Y): 
    dist = {}
    pai = {}
    vis = set()
    vis.add(o)
    dist[o] = 0
    queue = [o] 
    while queue:
        x,y = queue.pop(0) 
        if x > 0 and mapa[y][x-1] <= succ(mapa[y][x]) and (x-1,y) not in vis:
            vis.add((x-1,y))
            pai[(x-1,y)] = (x,y)
            dist[(x-1,y)] = dist[(x,y)] + 1
            queue.append((x-1,y))
        if x < X-1 and mapa[y][x+1] <= succ(mapa[y][x]) and (x+1,y) not in vis:
            vis.add((x+1,y))
            pai[(x+1,y)] = (x,y)
            dist[(x+1,y)] = dist[(x,y)] + 1
            queue.append((x+1,y))
        if y > 0 and mapa[y-1][x] <= succ(mapa[y][x]) and (x,y-1) not in vis:
            vis.add((x,y-1))
            pai[(x,y-1)] = (x,y)
            dist[(x,y-1)] = dist[(x,y)] + 1
            queue.append((x,y-1))
        if y < Y-1 and mapa[y+1][x] <= succ(mapa[y][x]) and (x,y+1) not in vis:
            vis.add((x,y+1))
            pai[(x,y+1)] = (x,y)
            dist[(x,y+1)] = dist[(x,y)] + 1
            queue.append((x,y+1))
    return dist
        
 
for (y,l) in enumerate(sys.stdin):
    mapa[y] = {}
    for (x,c) in enumerate(l[:-1]):
        if c == 'S':
            o = (x,y)
            mapa[y][x] = 'a'
        elif c == 'E':
            d = (x,y)
            mapa[y][x] = 'z'
        else:
            mapa[y][x] = c

Y = len(mapa)
X = len(mapa[0])

ds = []
for x in range(X):
    for y in range(Y):
        if mapa[y][x] == 'a':
            dist = bfs((x,y),X,Y)
            if d in dist:
                ds.append(dist[d])

print(min(ds))
