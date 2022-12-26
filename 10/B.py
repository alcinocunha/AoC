import sys

X = 1
i = 0
for l in sys.stdin:
    if i >= X-1 and i <= X+1:
        print('#',end='')
    else:
        print('.',end='')
    if l[0:4] == "addx":
        _,n = l.split()
        i += 1
        if i >= 40:
            i = 0
            print()
        if i >= X-1 and i <= X+1:
            print('#',end='')
        else:
            print('.',end='')
        X += int(n)
    i += 1
    if i >= 40:
        i = 0
        print()