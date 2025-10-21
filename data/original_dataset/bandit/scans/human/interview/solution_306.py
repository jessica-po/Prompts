a, b, p, x = [int(x) for x in input().split()]

powers = [a]

while powers[-1] != 1:
    powers.append(powers[-1] * a % p)
    
order = len(powers)
powers = [powers[-1]] + powers

inverse = pow(order, p-2, p)

def f(sol):
    return (x // (p * order)) + (1 if sol <= x % (p * order) else 0)

def chinese(a, n, b, m):
    k = inverse * (b - a + m) % m
    x = k * n + a
    return x % (n * m)

res = 0
for i in range(len(powers)-1):
    inv = powers[order - i]
    val = inv * b % p
    
    sol = chinese(i, order, val, p)
    
    res += f(sol)
    
print(res)