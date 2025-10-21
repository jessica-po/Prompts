# cook your dish here
n=int(input())
s=list(map(int,input().split()))
su=0
for i in s:
    su+=i

an=(n)*(n+1)//2
if(an==su):
    print("YES")

else:
    print("NO")