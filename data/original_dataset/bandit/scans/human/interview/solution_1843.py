from math import floor,log
for _ in range(int(input())):
    n=int(input())
    p=(n*(n+1))//2
    f=floor(log(n,2))
    p-=2*(2**(f+1)-1)
    print(p)