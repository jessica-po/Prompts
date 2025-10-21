import math
a,b = [int(x) for x in input().split()]

area = a+b
t = int(math.sqrt(area))
sa = int(math.sqrt(a))
sb = int(math.sqrt(b))

D = []
DA = []
DB = []
for i in range(1,t+1):
    if area % i == 0:
        if i*i != area:
            D.append(i)
            D.append(area//i)
        else:
            D.append(i)

for i in range(1,sa+1):
    if a % i == 0:
        if i*i != a:
            DA.append(i)
            DA.append(a//i)
        else:
            DA.append(i)
            
for i in range(1,sb+1):
    if b % i == 0:
        if i*i != b:
            DB.append(i)
            DB.append(b//i)
        else:
            DB.append(i)
DA.sort()
DB.sort()
D.sort()

start = ((len(D)+1)//2)-1
div = len(D)

def closestdiv(t,D):
    low = 0
    high = len(D)-1
    while high - low > 1:
        guess = (high+low)//2
        if D[guess] > t:
            high = guess
        else:
            low = guess
    if D[high] <= t:
        return high
    else:
        return low
    
while start > -1:
    t = D[start]
    s = D[-start-1]
    if DA[-closestdiv(t,DA)-1] <= s:
        print(2*t+2*s)
        break
    elif DB[-closestdiv(t,DB)-1] <= s:
        print(2*t+2*s)
        break
    start -= 1