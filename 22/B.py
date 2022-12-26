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

"""
D = 4
def meta(c):
    if c == 1:
        return (D*2,0,[(6,2),(4,0),(3,3),(2,2)])
    if c == 2:
        return (0,D,[(3,0),(5,2),(6,1),(1,2)])
    if c == 3:
        return (D,D,[(4,0),(5,1),(2,0),(1,1)])
    if c == 4:
        return (2*D,D,[(6,1),(5,0),(3,0),(1,0)])
    if c == 5:
        return (2*D,2*D,[(6,0),(2,2),(3,3),(4,0)])
    if c == 6:
        return (3*D,2*D,[(1,2),(2,1),(5,0),(4,1)])

"""
# The following info must me coded by hand for each input
# side size
D = 50
# for each side return the up left side coordinates and
# wich side is next to each direction and how many rotations
# are needed to adjust the coordinates
def meta(c):
    if c == 1:
        return (D,0,[(2,0),(3,0),(4,2),(6,1)])
    if c == 2:
        return (D*2,0,[(5,2),(3,1),(1,0),(6,0)])
    if c == 3:
        return (D,D,[(2,3),(5,0),(4,3),(1,0)])
    if c == 4:
        return (0,D*2,[(5,0),(6,0),(1,2),(3,1)])
    if c == 5:
        return (D,2*D,[(2,2),(6,1),(4,0),(3,0)])
    if c == 6:
        return (0,3*D,[(5,3),(2,0),(1,3),(4,0)])

def rotate(n,x,y):
    for i in range(n):
        x,y = D-1-y,x
    return (x,y)

def cube(x,y):
    for c in range(1,7):
        dx,dy,_ = meta(c)
        if x >= dx and x < dx+D and y >= dy and y < dy+D:
            return (c,x-dx,y-dy)

def uncube(c,x,y):
    dx,dy,_ = meta(c)
    return (dx+x,dy+y)

def next(x,y,d):
    c,x,y = cube(x,y)
    _,_,t = meta(c)
    if d == 0:
        if x < D-1:
            return uncube(c,x+1,y),d
        else:
            q,r = t[d]
            x,y = rotate(r,0,y)
            return uncube(q,x,y),(d+r)%4
    if d == 1:
        if y < D-1:
            return uncube(c,x,y+1),d
        else:
            q,r = t[d]
            x,y = rotate(r,x,0)
            return uncube(q,x,y),(d+r)%4
    if d == 2:
        if x > 0:
            return uncube(c,x-1,y),d
        else:
            q,r = t[d]
            x,y = rotate(r,D-1,y)
            return uncube(q,x,y),(d+r)%4
    if d == 3:
        if y > 0:
            return uncube(c,x,y-1),d
        else:
            q,r = t[d]
            x,y = rotate(r,x,D-1)
            return uncube(q,x,y),(d+r)%4

c = 0
while c < len(cs):
    if cs[c] == 'R':
        d = (d+1)%4
        c += 1
    elif cs[c] == 'L':
        d = (d-1)%4
        c += 1
    else:
        e = c
        while (e < len(cs) and cs[e] != 'R' and cs[e] != 'L'):
            e += 1
        n = int(cs[c:e])
        for i in range(n):
            (nx,ny),dx = next(x,y,d)
            if mapa[ny][nx] == '#':
                break
            else:
                x,y,d = nx,ny,dx
        c = e

print((x+1)*4+(y+1)*1000+d)
