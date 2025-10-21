n = int(input())
a = [2, 3 ,5, 7]
ans = 0
import operator
import itertools
import functools
for i in range(1, 5):
    for p in itertools.combinations(a, i):
        x = functools.reduce(operator.mul, p)
        ans += (-1) ** (i + 1) * (n // x)

print(n - ans)