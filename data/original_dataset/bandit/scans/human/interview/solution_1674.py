def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

n, k = mi()
a = li()
s = input().strip()

ans = 0
i = 0
while i < n:
    j = i + 1
    while j < n and s[j] == s[i]:
        j += 1
    b = sorted(a[i:j])
    ans += sum(b[-k:])
    i = j
print(ans)