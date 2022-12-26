import sys

s = sys.stdin.readline()

for i in range(4,len(s)):
    if len(set(s[i-4:i])) == 4:
        break

print(i)