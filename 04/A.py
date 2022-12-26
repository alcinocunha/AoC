import sys

def contains(x,y):
    return x[0] <= y[0] and y[1] <= x[1]

r = 0
for l in sys.stdin:
    a,b = l.strip().split(',')
    x = list(map(int,a.split('-')))
    y = list(map(int,b.split('-')))
    if contains(x,y) or contains(y,x):
        r += 1
print(r)
