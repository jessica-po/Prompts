s=input()[::-1]
alist=[0]*2019
num1=0
num2=1/10
lens=len(s)
for i in range(lens):
  num2=int(((num2)*10)%2019)
  num1=(num1+int(s[i])*(num2))%2019
  alist[num1]+=1
alist[0]+=1
ans=0
for i in range(2019):
  ans+=alist[i]*(alist[i]-1)//2
print(ans)