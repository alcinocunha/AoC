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
    return map(lambda p: (p[0]-1,p[1]),figure(n,x,y))

def right(n,x,y):
    return map(lambda p: (p[0]+1,p[1]),figure(n,x,y))

def down(n,x,y):
    return map(lambda p: (p[0],p[1]-1),figure(n,x,y))

jet = sys.stdin.readline()[:-1]


mapa = set()

def ocupadas(l):
    return any([p in mapa or p[0] <= 0 or p[0] >= 8 or p[1] <= 0 for p in l])

def altura():
    return max([0]+[p[1] for p in mapa])

def draw():
    for y in range(altura(),0,-1):
        for x in range(1,8):
            if (x,y) in mapa:
                print('#',end='')
            else:
                print('.',end='')
        print()
    print()

j = 0
for i in range(2022):
    n = i%5
    h = altura()
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

print(altura())




