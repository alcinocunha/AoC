import sys

expr = {}

for l in sys.stdin:
    if l[6].isdigit():
        expr[l[0:4]] = int(l[6:])
    elif l[11] =='+':
        expr[l[0:4]] = (lambda x,y: x+y, l[6:10],l[13:17])
    elif l[11] == '-':
        expr[l[0:4]] = (lambda x,y: x-y, l[6:10],l[13:17])
    elif l[11] == '*':
        expr[l[0:4]] = (lambda x,y: x*y, l[6:10],l[13:17])
    else:
        expr[l[0:4]] = (lambda x,y: x//y, l[6:10],l[13:17])

def calc(n):
    if type(expr[n]) is int:
        return expr[n]
    else:
        return expr[n][0](calc(expr[n][1]),calc(expr[n][2]))

print(calc('root'))