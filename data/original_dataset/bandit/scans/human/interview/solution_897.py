n, m = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

mult = 1
mod = 10 ** 9 + 7
res = 0

m_inv = pow(m, mod - 2, mod)

for x, y in zip(a, b):
    if x and y:
        if x > y:
            res += mult
            res %= mod
            break
        elif x == y:
            continue
        else:
            break
    elif x:
        res += mult * (x-1) * m_inv % mod
        res %= mod
        mult = mult * m_inv % mod
    elif y:
        res += mult * (m - y) * m_inv % mod
        res %= mod
        mult = mult * m_inv % mod
    else:
        res += mult * m * (m - 1) // 2 * m_inv * m_inv % mod
        res %= mod
        mult = mult * m_inv % mod
print(res)