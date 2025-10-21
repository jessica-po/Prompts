k=int(input())

L={}
s=".123456789"
for item in s:
    L[item]=0
for i in range(4):
    s=input()
    for item in s:
        L[item]+=1

s="123456789"
done=True
for item in s:
    if(L[item]>2*k):
        print("NO")
        done=False
        break
if(done):
    print("YES")