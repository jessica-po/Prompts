n = int(input())
a, b = input(), input()
t = {i + j: 0 for i in '01' for j in '01'}
for i in range(2 * n): t[a[i] + b[i]] += 1
d = t['11'] & 1
d += (t['10'] - t['01'] + 1 - d) // 2
if d > 0: d = 1
elif d < 0: d = 2
print(['Draw', 'First', 'Second'][d])