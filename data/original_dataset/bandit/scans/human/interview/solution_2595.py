ans = []
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    a, b = max(a, b), min(a, b)
    if a % b != 0:
        ans.append(-1)
        continue
    x = a // b
    cnt = 0
    while x % 2 == 0:
        x //= 2
        cnt += 1
    if x != 1:
        ans.append(-1)
        continue
    ansi = (cnt - 1) // 3 + 1
    ans.append(ansi)
print('\n'.join(map(str, ans)))