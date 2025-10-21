N=int(input())
S=input()

ans=S[0]
for s in S:
  if ans[-1]!=s:
    ans+=s
print(len(ans))