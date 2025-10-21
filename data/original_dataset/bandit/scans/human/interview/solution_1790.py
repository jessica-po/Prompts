n = int(input())
d = {}
for i in range(n):
    s = input().split()
    for j in range(int(s[0])):
        d[s[j+1]] = d.get(s[j+1],0)+1
ans = ""
for x in d:
    if d[x] == n:
        ans += str(x) + ' '
print(ans.strip())