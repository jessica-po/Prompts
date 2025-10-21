from queue import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

used = set(arr)
q = deque()
for i in range(n):
    q.append([arr[i] - 1, 1, -1])
    q.append([arr[i] + 1, 1, 1])

ret = []
s = 0
while m:
    x, l, dr = q.popleft()
    a = x + dr
    if not a in used:
        q.append([a, l + 1, dr])
    if not x in used:
        used.add(x)
        ret.append(x)
        m -= 1
        s += l
print(s)
print(*ret)