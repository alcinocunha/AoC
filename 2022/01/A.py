import sys

m = 0
e = 0

for l in sys.stdin:
    if len(l) == 1:
        e = 0
    else:
        e += int(l[:-1])
    if e > m:
        m = e
        
print(m)
    