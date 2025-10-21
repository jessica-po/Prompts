import math
n=int(input())
ans=0
num=int(math.sqrt(n)+1)
for i in range(1,num)[::-1]:
    if n%i==0:
        ans=i+(n//i)-2
        break
print(ans)