n = int(input())
st = input()
ans = n
i = 1
while i < n:
    if st[i - 1] != st[i]:
        ans -= 1
        i += 1
    i += 1
print(ans)