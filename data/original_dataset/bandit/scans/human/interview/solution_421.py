def key_tri(argument):
    return argument[1]

n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]
L.sort(key=key_tri)
r = 1
t = L[0][1]
for k in range(1,n):
    if L[k][0]>t:
        r+=1
        t = L[k][1]
print(r)