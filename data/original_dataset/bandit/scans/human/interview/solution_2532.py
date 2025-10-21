p,q=list(map(int,input().split()))
if(p!=0):
 a=list(map(int,input().split()))
if(q!=0):
 b=list(map(int,input().split()))
 d=list(map(int,input().split()))
s=list(map(int,input().split()))
for i in range(10):
 c=0
 for j in range(1,p+1):
  c+=s[len(s)-j]*a[j-1]
 for k in range(0,q):
  c+=b[k]*d[k]**(i+10)
 s.append(c%10**6)
s=list([str(x) for x in s])
print(' '.join(s[10:21]))