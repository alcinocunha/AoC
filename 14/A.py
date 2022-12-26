import sys

mapa = set()

for l in sys.stdin:
    ps = [list(map(int,p.split(','))) for p in l.split(' -> ')]
    for i in range(1,len(ps)):
        if ps[i][0] == ps[i-1][0]:
            if ps[i][1] > ps[i-1][1]:
                s = 1
            else:
                s = -1
            for y in range(ps[i-1][1],ps[i][1]+s,s):
                mapa.add((ps[i][0],y))
        else:
            if ps[i][0] > ps[i-1][0]:
                s = 1
            else:
                s = -1
            for x in range(ps[i-1][0],ps[i][0]+s,s):
                mapa.add((x,ps[i][1]))

Y = max(map(lambda p: p[1],mapa))

i = 0
y = 0
while y < Y:
    x,y = 500,0
    while y < Y:
        if (x,y+1) not in mapa:
            y = y+1
        elif (x-1,y+1) not in mapa:
            x = x-1
            y = y+1
        elif (x+1,y+1) not in mapa:
            x = x+1
            y = y+1
        else:
            mapa.add((x,y))
            i += 1
            break
        
print(i)