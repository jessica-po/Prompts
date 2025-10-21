s = input()
res = []
i = 0
j = len(s)-1
while i<j:
    if s[i]=="(" and s[j]==")":
        res.append(i+1)
        res.append(j+1)
        i+=1
        j-=1
    else:
        if s[i]==")":
            i+=1
        else:
            j-=1

if len(res)==0:
    print(0)
else:
    print(1)
    print(len(res))
    res.sort()
    print(*res,sep=" ")