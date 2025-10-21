import math

N = int(input())

def f(a,b):
    if len(str(a)) < len(str(b)):
        return len(str(b))
    else:
        return len(str(a))

ans = 100000000000
for i in range(1,int(math.sqrt(N)+1)):
    if N % i == 0:
        ans = min(ans,f(i,N//i))
print(ans)