import sys

def score(x,y):
    if y == 'X':
        if x == 'A':
            return 0+3
        if x == 'B':
            return 0+1
        if x == 'C':
            return 0+2
    if y == 'Y':
        if x == 'A':
            return 3+1
        if x == 'B':
            return 3+2
        if x == 'C':
            return 3+3
    if y == 'Z':
        if x == 'A':
            return 6+2
        if x == 'B':
            return 6+3
        if x == 'C':
            return 6+1

total = 0
for l in sys.stdin:
    total += score(l[0],l[2])
print(total)