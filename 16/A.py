import sys
from itertools import permutations 

adj = {}
pressure = {}

for l in sys.stdin:
    n = l[6:8]
    p = int(l[23:].split(';')[0])
    pressure[n] = p
    _,a = l.split('valve')
    if a[0] == 's':
        adj[n] = a[2:-1].split(', ')
    else:
        adj[n] = a[1:-1].split(', ')

dist = {}
for o in adj: 
    dist[o] = {}
    for d in adj: 
        if o == d:
            dist[o][d] = 0 
        elif d in adj[o]:
            dist[o][d] = 1
        else:
            dist[o][d] = float("inf") 
for k in adj:
    for o in adj:
        for d in adj:
            if dist[o][k] + dist[k][d] < dist[o][d]: 
                dist[o][d] = dist[o][k] + dist[k][d]

valves = list(sorted([n for n in pressure if pressure[n] > 0], key = lambda n : -pressure[n]))

def search(t,n,valves,f):
    if t == 0:
        return f
    m = f * t
    for i in range(len(valves)):
        d = valves[i]
        if dist[n][d]+1 < t:
            del valves[i]
            m = max(m,f * (dist[n][d] + 1) + search(t - (dist[n][d] + 1),d,valves,f + pressure[d]))
            valves.insert(i,d)
    return m

print(search(30,'AA',valves,0))
