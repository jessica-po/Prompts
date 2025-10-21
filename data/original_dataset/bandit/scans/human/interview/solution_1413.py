n = int(input())
s = input()
r = 0
for i in range(n):
    if s[i] in '2468':
        r += i + 1
print(r)