#Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys, math, queue
#sys.stdin = open("input.txt", "r")
MOD = 10**9+7

n = int(input())
p = []
for i in range(n):
    x, y = map(int, input().split())
    p.append((x, y))

d = {}

for i in range(n):
    x1, y1 = p[i]
    for j in range(i+1, n):
        x2, y2 = p[j]
        if x1 != x2:  
            m = (y2-y1)/(x2-x1)
            c = (y1*x2-x1*y2)/(x2-x1)
        else:
            m = 10**10
            c = x1
        if m in d:
            if c in d[m]:
                d[m][c] += 1
            else:
                d[m][c] = 1
        else:
            d[m] = {c: 1}

p = []
for m in d:
    p.append(len(d[m]))
s = sum(p)
ans = 0
for x in p:
    ans += x*(s-x)
print(ans//2)