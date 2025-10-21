s = input()
res = set()
for i in range(len(s) + 5):
    s = s[1:] + s[0]
    res.add(s)
print(len(list(res)))