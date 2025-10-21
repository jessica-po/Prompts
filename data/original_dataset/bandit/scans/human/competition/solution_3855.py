import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

n=int(input())

ans=1
while 2**ans-1<n:
    ans+=1
print(ans)