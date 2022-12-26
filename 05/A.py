import sys

# number of stacks
n = 9
# max height
m = 8

stacks = [[] for i in range(n)]

for i in range(m):
    l = sys.stdin.readline()
    for j in range(n):
        if l[j*4+1] != ' ':
            stacks[j].insert(0,l[j*4+1])

sys.stdin.readline()
sys.stdin.readline()

for l in sys.stdin:
    _,q,_,o,_,d = l.split()
    for i in range(int(q)):
        c = stacks[int(o)-1].pop()
        stacks[int(d)-1].append(c)
 
s = [stacks[i].pop() for i in range(n) if stacks[i]]
print(''.join(s))