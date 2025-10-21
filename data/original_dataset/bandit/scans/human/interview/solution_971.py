# You lost the game.
n,b,d = list(map(int, input().split()))
L = list(map(int, input().split()))
r = 0
c = 0
for i in range(n):
    if L[i] <= b:
        c += L[i]
        if c > d:
            r += 1
            c = 0
print(r)