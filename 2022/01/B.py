import sys

elves = []
e = 0

for l in sys.stdin:
    if len(l) == 1:
        elves.append(e)
        e = 0
    else:
        e += int(l[:-1])
else:
    elves.append(e)
    
elves.sort(reverse = True)
total = sum(elves[:3])
print(total)