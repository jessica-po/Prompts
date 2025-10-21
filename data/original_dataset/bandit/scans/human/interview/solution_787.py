import sys

#fin = open("input.txt", 'r')
fin = sys.stdin

n = int(fin.readline())
s = fin.readline().strip()
i = 1
cur = 0
used = {c: False for c in "qwertyuiopasdfghjklzxcvbnm"}
starts = [0]
used[s[0]] = True
while i < len(s) and cur < n - 1:
    if not used[s[i]]:
        used[s[i]] = True
        starts.append(i)
        cur += 1
    i += 1
if cur < n - 1:
    print("NO")
else:
    print("YES")
    starts.append(len(s))
    for i in range(len(starts) - 1):
        print(s[starts[i]:starts[i + 1]])