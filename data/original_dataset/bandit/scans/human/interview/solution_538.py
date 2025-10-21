n = input()
n = n.strip('0')
print('YES' if n == n[::-1] else 'NO')