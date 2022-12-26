import sys

def digit(c):
    if c == '2':
        return 2
    if c == '1':
        return 1
    if c == '0':
        return 0
    if c == '-':
        return -1
    if c == '=':
        return -2

def s2d(s):
    r = 0
    for i,c in enumerate(reversed(s)):
        r += digit(c)*(5**i)
    return r

def d2s(n):
    l = []
    while n > 0:
        r = n % 5
        if r == 0:
            l.insert(0,'0')
            n = n // 5
        if r == 1:
            l.insert(0,'1')
            n = n // 5
        if r == 2:
            l.insert(0,'2')
            n = n // 5
        if r == 3:
            l.insert(0,'=')
            n = (n // 5) + 1
        if r == 4:
            l.insert(0,'-')
            n = (n // 5) + 1
    return ''.join(l)


t = 0
for s in sys.stdin:
    t += s2d(s[:-1])

print(d2s(t))