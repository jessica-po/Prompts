n = int(input())
s = input()
i = 0
d = 1
t = []
while i < n:
    t.append(s[i])
    i += d
    d += 1

print(''.join(t))