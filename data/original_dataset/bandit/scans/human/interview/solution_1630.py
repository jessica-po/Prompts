n = int(input())
first = {}
second = set()
s1 = [0] * n
ans = [0] * n
for i in range(n):
    a, b = input().split()
    a = a[:3]
    b = b[0]
    s1[i] = b
    if a in first.keys():
        first[a].append(i)
    else:
        first[a] = [i]
        ans[i] = a
F = True
for name in first.keys():
    if not F:
        break
    if len(first[name]) > 1:
        for i in first[name]:
            c = name[:2] + s1[i]
            if c in second:
                F = False
                break
            else:
                second.add(c)
                ans[i] = c
        first[name] = 0

def process(name):
    nonlocal F
    if F == False:
        return
    if first[name] != 0 and name in second:
        t = first[name][0]
        c = name[:2] + s1[t]
        if c in second:
            F = False
            return
        else:
            second.add(c)
            ans[t] = c
            first[name] = 0
            if c in first.keys() and first[c] != 0:
                process(c)
                


for name in first.keys():
    process(name)
                

if F:
    print('YES')
    for i in range(n):
        print(ans[i])
else:
    print('NO')