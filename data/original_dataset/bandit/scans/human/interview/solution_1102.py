n, a = list(map(int, input().split()))
x = list(map(int, input().split()))

a -= 1

result = x[a]

for i in range(1, n + 1):
    le = a - i
    rg = a + i

    le_i = le >= 0 and le < n
    rg_i = rg >= 0 and rg < n
    if not le_i and not rg_i:
        break

    if le_i and not rg_i:
        result += x[le]
    elif not le_i and rg_i:
        result += x[rg]
    else:
        if x[le] == x[rg] == 1:
            result += 2

print(result)