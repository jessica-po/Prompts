rest, people = map(int, input().split())
types = list(map(int, input().split()))
a = dict()
for elem in types:
    if elem in a:
        a[elem] += 1
    else:
        a[elem] = 1
maximum = 0
for key in a:
    if a[key] > maximum:
        maximum = a[key]
needed = maximum
while needed % people != 0:
    needed += 1
ans = 0
for key in a:
    ans += needed - a[key]
print(ans)