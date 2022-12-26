import sys
import string

def common(s,t):
    for c in s:
        if c in t:
            return c

def priority(c):
    if c.islower():
        return ord(c)-ord('a')+1
    else:
        return ord(c)-ord('A')+27

t = 0
for l in sys.stdin:
    m = len(l)//2
    t += priority(common(l[:m],l[m:]))
print(t)