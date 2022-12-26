import sys
import string

def common(s,t,u):
    return set(s).intersection(set(t).intersection(set(u))).pop()

def priority(c):
    if c.islower():
        return ord(c)-ord('a')+1
    else:
        return ord(c)-ord('A')+27

t = 0
g = []
for l in sys.stdin:
    g.append(l[:-1])
    if len(g) == 3:
        t += priority(common(g[0],g[1],g[2]))
        g.clear()
print(t)