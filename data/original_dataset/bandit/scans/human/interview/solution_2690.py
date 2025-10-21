# cook your dish here
st=input().strip()
b=[]
for i in range(len(st)):
    for j in range(i+1,len(st)):
        if st[i]!=st[j]:
            z=abs(i-j)
            b.append(z)
print(max(b))