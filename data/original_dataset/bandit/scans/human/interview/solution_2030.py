def tle():
    k=0
    while (k>=0):
        k+=1
def quad(a, b, c):
    disc = (b**2-4*a*c)
    if disc<0:
        disc=0
        
    disc = (disc)**0.5
    
    return ((-b+disc)/2/a, (-b-disc)/2/a)

x = int(input())
y = list(map(float, input().strip().split(' ')))
z = list(map(float, input().strip().split(' ')))

py = [0, y[0]]
for i in range(1, x):
    py.append(py[-1]+y[i])
z.reverse()
pz = [0, z[0]]
for i in range(1, x):
    pz.append(pz[-1]+z[i])
pz.reverse()
k = []
for i in range(0, x+1):
    k.append(py[i]+1-pz[i])
l = [0]
for i in range(x):
    l.append(k[i+1]-k[i])
    #a[i]+b[i]

s1 = 0
s2 = 0
avals = []
bvals = []

for i in range(1, x+1):
    a, b = (quad(-1, s1+l[i]-s2, (s1+l[i])*s2-py[i]))
    
    if b<0 or l[i]-b<0:
        a, b = b, a
    if a<0 and b<0:
        a=0
        b=0
    bvals.append(b)
    avals.append(l[i]-b)
    s1+=avals[-1]
    s2+=bvals[-1]
    
for i in range(len(avals)):

    if abs(avals[i])<=10**(-10):
        avals[i] = 0
    if abs(bvals[i])<=10**(-10):
        bvals[i] = 0
        
print(' '.join([str(i) for i in avals]))
print(' '.join([str(i) for i in bvals]))