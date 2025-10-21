s,p=map(int,input().split())
import math
for i in range(1,math.floor(p**0.5)+1):
    if p%i==0 and p//i+i==s:
        print("Yes")
        return
print("No")