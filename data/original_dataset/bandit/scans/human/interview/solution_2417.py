n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
fined=0
i=0
j=0
d1={}
while i<n and j<n:
    if l1[i] in d1:
        i+=1
        continue
    if l1[i]==l2[j]:
        i+=1
        j+=1
    else :
        while j<n and l2[j]!=l1[i]:
            d1[l2[j]]=1
            j+=1
            fined+=1
print(fined)