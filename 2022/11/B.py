import sys

# number of monkeys
N = 8

items = {}
op = {}
test = {}
ift = {}
iff = {}

insp = {}

def readMonkey(i):
    sys.stdin.readline()
    _,s = sys.stdin.readline().split(': ')
    items[i] = list(map(int,s.split(', ')))
    _,s = sys.stdin.readline().split('old ')
    if (s[0] == '*'):
        if s[2:-1] == 'old':
            op[i] = lambda x : x * x
        else:
            op[i] = lambda x,s=s: x * int(s[2:-1])
    else:
        if s[2:-1] == 'old':
            op[i] = lambda x : x + x
        else:
            op[i] = lambda x,s=s: x + int(s[2:-1])
    _,s = sys.stdin.readline().split('by ')
    test[i] = int(s[:-1])
    _,s = sys.stdin.readline().split('monkey ')
    ift[i] = int(s[:-1])
    _,s = sys.stdin.readline().split('monkey ')
    iff[i] = int(s[:-1])
    sys.stdin.readline()
        
prod = 1

for i in range(N):
    readMonkey(i)
    insp[i] = 0
    prod *= test[i]


for r in range(10000):
    for i in range(N):
        for x in items[i]:
            insp[i] += 1
            w = op[i](x) % prod
            if w % test[i] == 0:
                items[ift[i]].append(w)
            else:
                items[iff[i]].append(w)
        items[i] = []

cs = list(insp.values())
cs.sort(reverse=True)
print(cs[0]*cs[1])