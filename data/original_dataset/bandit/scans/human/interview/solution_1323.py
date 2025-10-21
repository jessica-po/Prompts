import sys

n,m=list(map(int,sys.stdin.readline().split()))



A=list(map(int,sys.stdin.readline().split()))



B=list(map(int,sys.stdin.readline().split()))





A.sort(reverse=True)

B.sort(reverse=True)

a=sum(A)

b=sum(B)

ans=0

left=0

for i in range(n):

    left+=A[i]

    temp=b*(i+1)+a-left

    if(ans==0):

        ans=temp

    ans=min(ans,temp)



left=0

for i in range(m):

    left+=B[i]

    temp=a*(i+1)+b-left

    if(ans==0):

        ans=temp

    ans=min(ans,temp)

print(ans)

    





# Made By Mostafa_Khaled