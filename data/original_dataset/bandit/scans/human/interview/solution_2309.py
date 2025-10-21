n=int(input())
la=[]
le=[]
li=[]
lo=[]
lu=[]
ans=[]
d1={}
for i in range(n):
    s=input()
    x=s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')
    if x>0:
        
        for c in s[::-1]:
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
                break
        if (x,c) in d1:
            d1[(x,c)].append(s)
        else :
            d1[(x,c)]=[s]
d2={}
pairs1=[]
pairs2=[]
for k in d1:
    if len(d1[k])%2==1:
        if k[0] in d2:
            d2[k[0]].append(d1[k][0])
        else :
            d2[k[0]]=[d1[k][0]]
        for i in range(1,len(d1[k]),2):
            pairs1.append((d1[k][i],d1[k][i+1]))
    else :
        for i in range(0,len(d1[k]),2):
            pairs1.append((d1[k][i],d1[k][i+1]))
for k in d2:
    if len(d2[k])>1:
        if len(d2[k])%2==1:
            d2[k].pop()
        for i in range(0,len(d2[k]),2):
            pairs2.append((d2[k][i],d2[k][i+1]))
if len(pairs1)<len(pairs2):
    print(len(pairs1))
    for i in range(len(pairs1)):
        print(pairs2[i][0],pairs1[i][0])
        print(pairs2[i][1],pairs1[i][1])
else :
    print(len(pairs2)+(len(pairs1)-len(pairs2))//2)
    for i in range(len(pairs2)):
        print(pairs2[i][0],pairs1[i][0])
        print(pairs2[i][1],pairs1[i][1])
    for j in range(len(pairs2),len(pairs1),2):
        if j==len(pairs1)-1:
            break
        else :
            print(pairs1[j][0],pairs1[j+1][0])
            print(pairs1[j][1],pairs1[j+1][1])