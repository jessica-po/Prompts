def mi():
    return map(int, input().split())
 
'''
5
1 2 3 4 5
'''
for _ in range(1):
    n = int(input())
    a = list(mi())
    a.sort()
    k = 0
    out = [0]*n
    for i in range(1,n,2):
        out[i] = a[k]
        k+=1
    for i in range(0,n,2):
        out[i] = a[k]
        k+=1
    ans = 0
    a = out
    for i in range(1,n-1):
        if a[i]<a[i-1] and a[i]<a[i+1]:
            ans+=1
    print (ans)
    print (*out)