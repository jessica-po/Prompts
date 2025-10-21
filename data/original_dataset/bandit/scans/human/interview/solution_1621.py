s = input().strip()
k = int(input())
w = list(map(int, input().split()))
f = 0
m = max(w)
for i in range(len(s)):
    f += (i + 1) * w[ord(s[i]) - ord('a')]
for i in range(len(s), len(s) + k):
    f += (i + 1) * m
print(f)