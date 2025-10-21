import sys
l,r=map(int,(sys.stdin.readline().split()))
i=64
while i>=0:
    if ((1<<i)&l!=0 and (1<<i)&r!=0) or ((1<<i)&l==0 and (1<<i)&r==0):i-=1
    else:break
print((1<<(i+1))-1)