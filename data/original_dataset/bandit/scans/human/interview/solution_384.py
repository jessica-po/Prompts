# You lost the game.

n = int(input())
s = str(input())

R = []
b = 0
for i in range(n):
    if s[i] == "B":
        b += 1
    elif b > 0:
        R += [b]
        b = 0
if b > 0:
    R += [b]
print(len(R))
for i in range(len(R)):
    print(R[i],end=" ")