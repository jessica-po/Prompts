from fractions import gcd
n=int(input())
a=list(map(int,input().split()))
no=a[0]
for i in range(1,n):
    no=gcd(no,a[i])
print(no*n)