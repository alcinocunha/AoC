import sys
import ast

def ok(l,r):
    if type(l) is int and type(r) is int:
        if l < r:
            return -1
        elif l > r:
            return 1
        else:
            return 0
    if type(l) is int:
        return ok([l],r)
    if type(r) is int:
        return ok(l,[r])
    if not l and not r:
        return 0
    if not l:
        return -1
    if not r:
        return 1
    if ok(l[0],r[0]) == 0:
        return ok(l[1:],r[1:])
    return ok(l[0],r[0])
    
i = 0
sum = 0
l = sys.stdin.readline()
while l:
    i += 1
    r = sys.stdin.readline()
    if ok(ast.literal_eval(l),ast.literal_eval(r)) < 0:
        sum += i
    sys.stdin.readline()
    l = sys.stdin.readline()

print(sum)