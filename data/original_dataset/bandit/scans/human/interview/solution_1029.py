s=input().strip()
n=len(s)
i=0
k=1
j=0
while i<n:
    #print(i,j)
    j=i
    i+=1
    while i<n and s[i]=='0':
        i+=1
    if j>i-j:
        k+=1
    elif j==i-j:
        if s[:j]>=s[j:i]:
            k+=1
        else:
            k=1
    else:
        k=1
print(k)