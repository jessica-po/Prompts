n, k = map(int, input().split())
a    = list(map(int, input().split()))
a    = a[::-1]
s    = [a[0]]
S    = 0

for x in a[1:]:
    s.append(s[-1]+x)

S   += s[-1]
s.pop()
k   -= 1
s   = sorted(s)

i=0
while i<=k-1:
    S += s.pop()
    i += 1
print(S)