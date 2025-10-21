n = int(input())

s = input()
code = input()

res = 0
for i in range(n):
    k = abs(int(s[i]) - int(code[i]))
    res += min(k, 10 - k)

print(res)