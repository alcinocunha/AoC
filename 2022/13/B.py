import sys
import ast
import functools

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
    
ps = [[[2]],[[6]]]
l = sys.stdin.readline()
while l:
    ps.append(ast.literal_eval(l))
    r = sys.stdin.readline()
    ps.append(ast.literal_eval(r))
    sys.stdin.readline()
    l = sys.stdin.readline()

ps.sort(key=functools.cmp_to_key(ok))

for i in range(len(ps)):
    if ps[i] == [[2]]:
        begin = i+1
    if ps[i] == [[6]]:
        end = i+1

print(begin * end)