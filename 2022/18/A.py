import sys

cubes = set()

for l in sys.stdin:
    x,y,z = map(int,l.split(','))
    cubes.add((x,y,z))

r = 0
for (x,y,z) in cubes:
    for (a,b,c) in [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)]:
        if (a,b,c) not in cubes:
            r += 1

print(r)