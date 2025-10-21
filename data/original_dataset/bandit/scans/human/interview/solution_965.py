n=int(input())
a=input()
cnt=0
A=0
for i in range(0,n):
  if(a[i]=='I'): cnt+=1
  if(a[i]=='A'): A+=1
if(cnt==0):
    print(A)
elif(cnt==1):
    print(1)
else :print(0)