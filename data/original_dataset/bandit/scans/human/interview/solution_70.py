s = input().split()
k = int(s[1])
s = s[0]
if s.count('0') < k:
    if s.count('0') > 0:
        print(len(s) - 1)
    else:
        print(len(s))
    return
have = 0
its = 0
for i in range(len(s) - 1, -1, -1):
    its += 1
    if s[i] == '0':
        have += 1
    if have == k:
        print(its - have)
        return