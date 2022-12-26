import sys

def overlaps(x,y):
    return x[0] <= y[1] and y[0] <= x[1]

r = 0
for l in sys.stdin:
    a,b = l.strip().split(',')
    x = list(map(int,a.split('-')))
    y = list(map(int,b.split('-')))
    if overlaps(x,y):
        r += 1
print(r)
