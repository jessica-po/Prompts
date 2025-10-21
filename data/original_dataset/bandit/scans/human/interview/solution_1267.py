n=int(input())
s=set()
ar=list(map(int,input().split()))
for x in range(n):
    if(ar[x]!=0):
        s.add(ar[x])
print(len(s))