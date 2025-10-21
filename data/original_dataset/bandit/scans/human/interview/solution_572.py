def convert_to_binary(coef):
    res = []
    n = len(coef)
    carry = 0
    i = 0
    while i < n + 1000:
        if i >= n and not carry:
            break
        cur = carry
        if i < n:
            cur += coef[i]

        mod = cur % 2
        div = cur // 2
#        print(cur, div, mod)

        res.append(mod)

        carry = div

        i += 1
    return res, carry

n, k = list(map(int, input().split()))
coef = list(map(int, input().split()))

b, carry = convert_to_binary(coef)
ref = False
if carry < 0:
    b, carry = convert_to_binary(list([-x for x in coef]))
    ref = True


last = len(b) - 1
while b[last] != 1:
    last -= 1

ans = 0
for i in range(0, n + 1):
    if last - i > 40:
        continue

    cur = 0
    for j in range(i, last + 1):
        cur += b[j] * (2 ** (j - i))

    new_coef = coef[i] - cur
    if ref:
        new_coef = coef[i] + cur

    if abs(new_coef) > k:
        if b[i] == 1:
            break
        continue

    if i == n and new_coef == 0:
        if b[i] == 1:
            break
        continue

    ans += 1
    if b[i] == 1:
        break


print(ans)