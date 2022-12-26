import sys

X = 1
Xs = [1]

for l in sys.stdin:
    if l[:-1] == "noop":
        Xs.append(X)
    else:
        _,n = l.split()
        Xs.append(X)
        X += int(n)
        Xs.append(X)

t = 0
for i in range(20,221,40):
    t += i*Xs[i-1]

print(t)