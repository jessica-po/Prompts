N=int(input())
l=""
mod=10**9+7
Sa=list(input())
Sb=list(input())
for i in range(N):
   if Sa[i]==Sb[i]:
      l+="X"
   else:
      l+="Y"
l=l.replace("YY","Y")
ans=6 if l[0]=="Y" else 3
for i in range(1,len(l)):
   if l[i]=="Y" and l[i-1]=="Y":
      ans*=3
   if l[i]=="X" and l[i-1]=="X":
      ans*=2
   if l[i]=="Y" and l[i-1]=="X":
      ans*=2
   ans=ans%mod
print(ans)