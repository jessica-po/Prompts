# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
from itertools import accumulate

T = int(input())
#s = input()
#N,M,K,Q = [int(x) for x in stdin.readline().split()]
#arr = [int(x) for x in stdin.readline().split()]

check = [0]*45000

s = 0
for i in range(1,45001):
    s += i
    check[i-1] = s

for i in range(T):
    N = int(input())

    if N in check:
        idx = check.index(N)
        idx += 2
        print('1','3'*idx,'7',sep='',end='\n')

    else:
        # find largest number < N in check
        target = max(num for num in check if num < N)
        three = check.index(target)

        d = N - target

        print('1','3'*2,'7'*d,'3'*(three),'7',sep='',end='\n')