import sys

ore = {}
clay = {}
obsidian = {}

maxO = 0
maxC = 0
maxD = 0

i = 0
for l in sys.stdin:
    ore[i] = {}
    clay[i] = {}
    obsidian[i] = {}
    o,c,d,g = l.split('. ')
    ore[i]['o'] = int(o[34:].split()[0])
    maxO = max(maxO,ore[i]['o'])
    ore[i]['c'] = int(c[22:].split()[0])
    maxO = max(maxO,ore[i]['c'])
    ore[i]['d'] = int(d[26:].split()[0])
    maxO = max(maxO,ore[i]['d'])
    ore[i]['g'] = int(g[23:].split()[0])
    maxO = max(maxO,ore[i]['g'])
    clay[i]['d'] = int(d[26:].split()[3])
    maxC = max(maxC,clay[i]['d'])
    obsidian[i]['g'] = int(g[23:].split()[3])
    maxD = max(maxD,obsidian[i]['g'])
    i += 1

def search(i,t,ro,rc,rd,rg,o,c,d):
    if t == 0:
        return 0
    if (t,ro,rc,rd,rg,o,c,d) in memo:
        return memo[(t,ro,rc,rd,rg,o,c,d)]
    if ore[i]['g'] <= o and obsidian[i]['g'] <= d:
        r = rg+search(i,t-1,ro,rc,rd,rg+1,o+ro-ore[i]['g'],c+rc,d+rd-obsidian[i]['g'])
        memo[(t,ro,rc,rd,rg,o,c,d,g)] = r
        return r
    r = rg+search(i,t-1,ro,rc,rd,rg,o+ro,c+rc,d+rd)
    if ro < maxO and ore[i]['o'] <= o:
        r = max(r,rg+search(i,t-1,ro+1,rc,rd,rg,o+ro-ore[i]['o'],c+rc,d+rd))
    if rc < maxC and ore[i]['c'] <= o:
        r = max(r,rg+search(i,t-1,ro,rc+1,rd,rg,o+ro-ore[i]['c'],c+rc,d+rd))
    if rd < maxD and ore[i]['d'] <= o and clay[i]['d'] <= c:
        r = max(r,rg+search(i,t-1,ro,rc,rd+1,rg,o+ro-ore[i]['d'],c+rc-clay[i]['d'],d+rd))
    memo[(t,ro,rc,rd,rg,o,c,d)] = r
    return r
        
r = 1
for n in range(min(3,i)):
    memo = {}
    g = search(n,32,1,0,0,0,0,0,0)
    r *= g
print(r)


