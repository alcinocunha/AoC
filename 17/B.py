import sys

def figure(n,x,y):
    if n == 0:
        return [(x,y),(x+1,y),(x+2,y),(x+3,y)]
    if n == 1:
        return [(x+1,y),(x+1,y+1),(x+1,y+2),(x,y+1),(x+2,y+1)]
    if n == 2:
        return [(x,y),(x+1,y),(x+2,y),(x+2,y+1),(x+2,y+2)]
    if n == 3:
        return [(x,y),(x,y+1),(x,y+2),(x,y+3)]
    if n == 4:
        return [(x,y),(x+1,y),(x,y+1),(x+1,y+1)]

def left(n,x,y):
    return map(lambda p: (p[0]-1,p[1]), figure(n,x,y))

def right(n,x,y):
    return map(lambda p: (p[0]+1,p[1]), figure(n,x,y))

def down(n,x,y):
    return map(lambda p: (p[0],p[1]-1), figure(n,x,y))

jet = sys.stdin.readline()[:-1]

mapa = set()

def ocupadas(l):
    return any([p in mapa or p[0] <= 0 or p[0] >= 8 or p[1] <= 0 for p in l])

def altura():
    return max([0]+[p[1] for p in mapa])

m = {}
j = 0
H = 0
l = 0
i = 0
while i < 1000000000000:
    n = i%5
    h = altura()
    if n == 0 and (4,h) in mapa:
        if j in m:
            di = i-m[j][0]
            dh = h-m[j][1]
            r = 1000000000000-i
            i += (r // di) * di
            H += (r // di) * dh
        else:
            m[j] = (i,altura())
    x,y = 3,h+4
    while True:
        if jet[j] == '<':
            if not ocupadas(left(n,x,y)):
                x = x-1
        elif not ocupadas(right(n,x,y)):
            x = x+1
        j = (j+1) % len(jet)
        if not ocupadas(down(n,x,y)):
            y = y-1
        else:
            break
    mapa.update(figure(n,x,y))
    i += 1

H += altura()
print(H)