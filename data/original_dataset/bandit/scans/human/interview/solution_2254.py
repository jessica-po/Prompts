#!/usr/bin/env python3
import sys

def rint():
    return list(map(int, sys.stdin.readline().split()))
#lines = stdin.readlines()

def get_num1(i):
    cnt = 0
    while i:
        if i%2:
            cnt +=1
        i //=2
    return cnt

n = int(input())

a = list(rint())

b = [get_num1(aa) for aa in a]

ans = 0
#S0[i] : 1 if sum of 1s in ragne (0, i) is odd, else 0
S0 = [0]*n
S0[0] = b[0]%2
for i in range(1, n):
    S0[i] = (S0[i-1] + b[i])%2

#total even pairs in (0, n)
even_cnt = S0.count(0)

ans = even_cnt

# check total even pairs in (i, n)
for i in range(1, n):
    if b[i-1] %2:
        even_cnt = n - i - even_cnt
    else:
        even_cnt -= 1
    ans += even_cnt

for i in range(n):
    max_value = 0
    sum_value = 0
    for j in range(1, 62):
        if i + j > n:
            break
        sum_value += b[i+j-1]
        max_value = max(max_value, b[i+j-1])
        if 2 * max_value > sum_value and sum_value%2 == 0:
            ans -= 1

print(ans)