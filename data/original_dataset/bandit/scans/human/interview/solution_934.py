c = input()
s = list(input().split())
print('YES' if any(c[0] == x[0] or c[1] == x[1] for x in s) else 'NO')