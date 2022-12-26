import sys

x = {}
y = {}
for i in range(10):
    x[i] = 0
    y[i] = 0
vis = set()
vis.add((0,0))

for l in sys.stdin:
    c,n = l.split()
    for i in range(int(n)):
        if c == 'R':
            x[0] += 1
        if c == 'L':
            x[0] -= 1
        if c == 'U':
            y[0] += 1
        if c == 'D':
            y[0] -= 1
        for t in range(1,10):        
            if not (abs(x[t]-x[t-1]) <= 1 and abs(y[t]-y[t-1]) <= 1):
                if y[t-1] > y[t]:
                    y[t] += 1
                if y[t-1] < y[t]:
                    y[t] -= 1
                if x[t-1] > x[t]:
                    x[t] += 1
                if x[t-1] < x[t]:
                    x[t] -= 1              
        vis.add((x[9],y[9]))

print(len(vis))
