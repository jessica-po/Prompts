n = int(input())

candies = list(map(int, input().strip().split()))

def intkoren(n):
    k = int(n**0.5)
    while (k+1)*(k+1) <= n:
        k += 1
    while k*k > n:
        k -= 1
    return k

cnt1 = 0
cnt2 = 0
new = []
for e in candies:
    u = intkoren(e)
    if e == 0:
        new.append((2,1))
        cnt1 += 1
    elif u*u == e:
        new.append((1,1))
        cnt1 += 1
    else:
        mini = min(e - u*u, (u+1)*(u+1)-e)
        new.append((mini, -1))
        cnt2 += 1

new.sort()

#print(new, cnt1,cnt2)

count = 0
if cnt1 >= cnt2:
    todo = (cnt1 - cnt2)//2
    for steps, v in new:
        if todo == 0:
            break
        if v == 1:
            count += steps
            todo -= 1
else:
    todo = (cnt2 - cnt1)//2
    for steps,v in new:
        if todo == 0:
            break
        if v == -1:
            count += steps
            todo -= 1
print(count)