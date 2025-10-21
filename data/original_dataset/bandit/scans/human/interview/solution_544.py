def valid(a, b):
    d = abs(ord(a) - ord(b))
    return d == 0 or d == 2

T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    val = all(valid(s[i], s[n - i - 1]) for i in range(n))
    print('YES' if val else 'NO')