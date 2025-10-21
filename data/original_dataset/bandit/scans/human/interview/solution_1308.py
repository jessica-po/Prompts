def getIntList():
    return list(map(int, input().split()));
def getTransIntList(n):
    first=getIntList();
    m=len(first);
    result=[[0]*n for _ in range(m)];
    for i in range(m):
        result[i][0]=first[i];
    for j in range(1, n):
        curr=getIntList();
        for i in range(m):
            result[i][j]=curr[i];
    return result;
n, m = getIntList()
s=input();
orda=ord('a');
a=[ord(s[i])-orda for i in range(n)];
countSame=[1]*n;
upLim=0;
for lowLim in range(n):
    if lowLim<upLim:
        continue;
    for upLim in range(lowLim+1, n):
        if a[upLim]!=a[lowLim]:
            break;
    else:
        upLim+=1;
    for i in range(lowLim, upLim):
        countSame[i]=upLim-i;
def test(x, y, l):
    map1=[0]*27;
    map2=[0]*27;
    count=0;
    lowLim=min(countSame[x], countSame[y])-1;
    for i in range(lowLim, l):
        x1=map1[a[x+i]];
        x2=map2[a[y+i]];
        if x1!=x2:
            return 'NO';
        if x1==0:
            count+=1;
            map1[a[x+i]]=count;
            map2[a[y+i]]=count;
    return 'YES';
results=[];
for _ in range(m):
    x, y, l=getIntList();
    results.append(test(x-1, y-1, l));
print('\n'.join(results));