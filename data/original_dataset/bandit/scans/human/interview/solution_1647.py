# import sys
# sys.stdin = open('in.txt', 'r')

_ = input()
s = input()
t = input()

par = [i for i in range(26)]
def find(x):
    if par[x] != x:
        par[x] = find(par[x])
        return par[x]
    else:
        return x

for i in range(len(s)):
    a, b = find(ord(s[i])-97), find(ord(t[i])-97)
    if a != b:
        par[a] = b

res = 0
for i in range(26):
    find(i)

for i in range(26):
    res += max(0, par.count(i) - 1)
print(res)

for i in range(26):
    d = []
    for j in range(26):
        if par[j] == i:
            d.append(chr(j+97))

    for j in range(len(d)-1):
        print(d[j], d[j+1])