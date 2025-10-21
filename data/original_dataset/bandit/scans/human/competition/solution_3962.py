import sys
input = sys.stdin.readline

n=int(input())
lr=[list(map(int,input().split())) for i in range(n)]

L=[lr[i][0] for i in range(n)]
R=[lr[i][1] for i in range(n)]
L.sort()
R.sort()

ANS=0

for i in range(n):
    ANS+=max(L[i],R[i])

print(ANS+n)