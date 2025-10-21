def binary(n):
    curr=0
    while(n>0):
        if(n%2):
            curr+=1
        n=n//2
    return curr
l=input().split()
n=int(l[0])
k=int(l[1])
l=input().split()
li=[int(i) for i in l]
arr=[]
for i in range(2**15):
    if(binary(i)==k):
        arr.append(i)
hashi=dict()
for i in li:
    if i in hashi:
        hashi[i]+=1
    else:
        hashi[i]=1
count=0
for i in hashi:
    for j in arr:
        if((i^j) in hashi):
            if((i^j)==i):
                count=count+(hashi[i]*(hashi[i]-1))
            else:
                count=count+(hashi[i]*hashi[i^j])
print(count//2)