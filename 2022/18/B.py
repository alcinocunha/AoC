import sys

cubes = set()

open = {(0,0,0)}
trapped = set()

for l in sys.stdin:
    x,y,z = map(int,l.split(','))
    cubes.add((x,y,z))

def reaches(o):
    vis = {o}
    queue = [o] 
    while queue:
        v = queue.pop(0)
        (x,y,z) = v
        if v in open:
            open.update(vis)
            return True
        for d in [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)]:
            if d not in cubes and d not in vis: 
                vis.add(d)
                queue.append(d)
    trapped.update(vis)
    return False

r = 0
for (x,y,z) in cubes:
    for v in [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)]:
        if v not in cubes and v not in trapped and reaches(v):
            r += 1
print(r)
