a, b, c, d = input(), input(), input(), input()
a = a + b[::-1]
x = "X"
for i in range(4):
    if a[i] == x:
        a = a[:i] + a[i + 1:]
        break
c = c + d[::-1]

for i in range(4):
    if c[i] == x:
        c = c[:i] + c[i + 1:]
        break
flag = False
for i in range(4):
    if a == c:
        flag = True
    c = c[1:] + c[0]
if flag:
    print("YES")
else:
    print("NO")