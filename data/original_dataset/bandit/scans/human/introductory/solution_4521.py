def bitadd(a,w,bit):
 
    x = a
    while x <= (len(bit)-1):
        bit[x] += w
        x += x & (-1 * x)
 
def bitsum(a,bit):
 
    ret = 0
    x = a
    while x > 0:
        ret += bit[x]
        x -= x & (-1 * x)
    return ret


n = int(input())

x = list(map(int,input().split()))
v = list(map(int,input().split()))

vlis = []
for i in v:
    vlis.append(i)
vlis.sort()
vdic = {}

for i in range(n):
    vdic[vlis[i]] = i+1
#print (vdic)



xv = []
for i in range(n):
    xv.append([x[i],v[i]])
xv.sort()

ans = 0
BIT = [0] * (n+1)
BIT2 = [0] * (n+1)
for i in range(n):

    x,v = xv[i]

    ans += x * bitsum(vdic[v],BIT2) - bitsum(vdic[v],BIT)
    bitadd(vdic[v] , x , BIT)
    bitadd(vdic[v] , 1 , BIT2)

print (ans)