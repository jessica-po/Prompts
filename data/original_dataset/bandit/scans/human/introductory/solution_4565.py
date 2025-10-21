n=int(input())
s=input()

cnt=s[1:].count("E")
ans=cnt

for i in range(1,n):
  if s[i-1]=="W":
    cnt+=1
  if s[i]=="E":
    cnt-=1
  ans=min(ans,cnt)

print(ans)