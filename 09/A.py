import sys

hx,hy = 0,0
tx,ty = 0,0
vis = set()
vis.add((tx,ty))

for l in sys.stdin:
    c,n = l.split()
    for i in range(int(n)):
        if c == 'R':
            hx += 1
        if c == 'L':
            hx -= 1
        if c == 'U':
            hy += 1
        if c == 'D':
            hy -= 1        
        if not (abs(tx-hx) <= 1 and abs(ty-hy) <= 1):
            if hy > ty:
                ty += 1
            if hy < ty:
                ty -= 1
            if hx > tx:
                tx += 1
            if hx < tx:
                tx -= 1              
            vis.add((tx,ty))

print(len(vis))
