n = int(input())
s = input()
for d in range(1, n+1):
    if n%d == 0:
        t1 = s[:d]
        t2 = s[d:]
        s = t1[::-1] + t2
print(s)