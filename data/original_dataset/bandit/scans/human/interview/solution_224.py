# You lost the game.

s = str(input())
n = len(s)
d = -1
r = 0
V = "AEIOUY"
for i in range(n):
    if V.count(s[i]):
        r = max(r,i-d)
        d = i
print(max(r, n-d))