import sys

expr = {}
op = {}

for l in sys.stdin:
    if l[6].isdigit():
        expr[l[0:4]] = int(l[6:])
    elif l[11] =='+':
        expr[l[0:4]] = (lambda x,y: x+y, l[6:10],l[13:17])
        op[l[0:4]] = '+'
    elif l[11] == '-':
        expr[l[0:4]] = (lambda x,y: x-y, l[6:10],l[13:17])
        op[l[0:4]] = '-'        
    elif l[11] == '*':
        expr[l[0:4]] = (lambda x,y: x*y, l[6:10],l[13:17])
        op[l[0:4]] = '*'
    else:
        expr[l[0:4]] = (lambda x,y: x//y, l[6:10],l[13:17])
        op[l[0:4]] = '/'


def calc(n):
    if type(expr[n]) is int:
        return expr[n]
    else:
        return expr[n][0](calc(expr[n][1]),calc(expr[n][2]))

def contains(n,m):
    if n == m:
        return True
    elif type(expr[n]) is int:
        return False
    else:
        return contains(expr[n][1],m) or contains(expr[n][2],m)

def solve(n,v):
    if n == 'humn':
        return v
    if contains(expr[n][1],'humn'):
        h = expr[n][1]
        o = expr[n][2]
        r = calc(o)
        if op[n] == '+':
            return solve(h,v-r)
        elif op[n] == '-':
            return solve(h,v+r)
        elif op[n] == '*':
            return solve(h,v//r)
        elif op[n] == '/':
            return solve(h,v*r)
    else:
        o = expr[n][1]
        h = expr[n][2]
        r = calc(o)
        if op[n] == '+':
            return solve(h,v-r)
        elif op[n] == '-':
            return solve(h,r-v)
        elif op[n] == '*':
            return solve(h,v//r)
        elif op[n] == '/':
            return solve(h,r//v)

if contains(expr['root'][1],'humn'):
    print(solve(expr['root'][1],calc(expr['root'][2])))
else:
    print(solve(expr['root'][2],calc(expr['root'][1])))
