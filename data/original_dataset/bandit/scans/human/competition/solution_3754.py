P,a,I=998244353,1,input
n=int(I())
d=list(map(int,I().split()))
s=sum(d)%P
for i in d:a=a*i%P
for i in range(n,2*n-2):a=a*(s-i)%P
print(a)