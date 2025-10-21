n, k = map(int, input().split())
s = set()
st = input()
inp = input().split()
for x in inp:
    s.add(x)
current, ans = 0, 0
for x in st:
    if x in s:
        current += 1
    else:
        ans += (current * (current + 1)) // 2
        current = 0
ans += (current * (current + 1)) // 2
print(ans)