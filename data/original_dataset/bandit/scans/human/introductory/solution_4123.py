n = int(input())
s = input()
a = [[0] * 26 for _ in range(26)]
for i in range(n -1):
    a[ord(s[i]) - ord('A')][ord(s[i + 1]) - ord('A')] += 1

mx = -1

for i in range(26):
    for j in range(26):
        if a[i][j] > mx:
            mx = a[i][j]
            ans = chr(i + ord('A')) + chr(j + ord('A'))

print(ans)