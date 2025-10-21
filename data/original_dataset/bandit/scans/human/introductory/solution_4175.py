import collections
n = int(input())
words = [input() for _ in range(n)]
ok = True
for i in range(n-1):
    if words[i][-1] != words[i+1][0]:
        ok = False
count = collections.Counter(words)
for i in count.values():
    if i != 1:
        ok = False
print("Yes" if ok else "No")