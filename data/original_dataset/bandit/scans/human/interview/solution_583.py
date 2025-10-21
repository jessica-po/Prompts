n = int(input())
st = input()
s = [0 if c == "(" else 1 for c in st]
if n % 2 != 0 or sum(s) != n//2:
    print(0)
    print(1,1)
    return
maxx = 0
ind = (0,0)
maxshift = 0
for shift in range(n):
    stack = 0
    x1 = -1
    x2 = -1
    sumzero = 0
    for i,c in enumerate(s):
        if s[(i+shift)%n] == 0:
            stack+=1
        else:
            stack-=1
        if stack == 0:
            sumzero+=1
        if stack < 0:
            x1 = i
            break
    stack = 0
    for i in range(n-1, -1, -1):
        if s[(i+shift)%n] == 1:
            stack+=1
        else:
            stack-=1
        if stack < 0:
            x2 = i
            break
    if x1 == -1 and x2 == -1 and stack == 0:
        if sumzero > maxx:
            maxx=sumzero
            ind = (0,0)
    if x1 == -1 or x2 == -1 or x1 == x2:
        continue
    stack = 0
    corr = True
    ans = 0
    for i in range(n):
        c = s[(i+shift)%n]
        
        if i == x1 or i == x2:
            c = 1-c
        if c == 0:
            stack += 1
        else:
            stack -= 1
        if stack == 0:
            ans+=1
        if stack == -1:
            corr = False
            break
    
    if not corr or stack > 0:
        continue
    if ans > maxx:
        maxshift = shift
        maxx = ans
        ind = ((x1+shift)%n, (x2+shift)%n)
print(maxx)
print(ind[0]+1,ind[1]+1)