import sys
from bisect import *
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
ans=n=int(input())
a=sorted(map(int,sys.stdin.readline().split()))
for i in range(n):ans=min(ans,n-bisect_right(a,a[i]*2)+i)
print(ans)