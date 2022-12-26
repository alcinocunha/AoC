import sys

numbers = list(enumerate(map(int,sys.stdin)))

N = len(numbers)

for x in list(numbers):
    i = numbers.index(x)
    _,c = x
    del numbers[i]
    p = (i+c) % (N-1)
    if p == 0:
        p = N-1
    numbers.insert(p,x)

aux = [p[1] for p in numbers]
i = aux.index(0)
print(aux[(i+1000)%N]+aux[(i+2000)%N]+aux[(i+3000)%N])