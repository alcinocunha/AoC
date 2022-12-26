import sys

sizes = {}

path = []

for l in sys.stdin:
    if l[:-1] == '$ cd ..':
        s = sizes['/'.join(path)]
        path.pop()
        sizes['/'.join(path)] += int(s)
    elif l[0:4] == '$ cd':
        path.append(l[5:-1])
        sizes['/'.join(path)] = 0
    elif l[0:4] == '$ ls' or l[0:3] == 'dir':
        continue
    else:
        s,_ = l.split()
        sizes['/'.join(path)] += int(s)
else:
    while len(path) > 1:
        s = sizes['/'.join(path)]
        path.pop()
        sizes['/'.join(path)] += int(s)

unused = 70000000 - sizes['/']
need = 30000000 - unused
dirs = [sizes[d] for d in sizes if sizes[d] >= need]
print(min(dirs))
