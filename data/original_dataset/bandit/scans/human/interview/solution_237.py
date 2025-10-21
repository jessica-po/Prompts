n, m, k = map(int, input().split())
ans = 1
m -= n
left = k - 1
right = n - k

put = 1
while (m >= put):
    m -= put
    ans += 1
    put += (left > 0) + (right > 0)
    if (left): left -= 1
    if (right): right -= 1
    if (left == right == 0):
        ans += (m // put)
        break
print(ans)