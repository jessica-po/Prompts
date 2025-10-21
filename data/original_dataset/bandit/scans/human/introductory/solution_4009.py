n, x, y = map(int, input().split())
s = input()[-x:]
res = s.count('1')
if s[-y - 1] == '1': res -= 1
else: res += 1
# print(s)
print(res)