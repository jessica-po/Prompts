n = int(input())
a = input()
s = input()
d1, d2 = [], []
for q in range(n):
    if a[q] == 'a' and s[q] == 'b':
        d1.append(q+1)
    elif a[q] == 'b' and s[q] == 'a':
        d2.append(q+1)
if (len(d1)+len(d2)) % 2 == 1:
    print(-1)
else:
    print((len(d1)+len(d2))//2+len(d1) % 2)
    for q in range(1, len(d1), 2):
        print(d1[q-1], d1[q])
    for q in range(1, len(d2), 2):
        print(d2[q-1], d2[q])
    if len(d1) % 2 == 1:
        print(d1[-1], d1[-1])
        print(d1[-1], d2[-1])