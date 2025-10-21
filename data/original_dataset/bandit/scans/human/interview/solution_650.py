p = "AEFHIKLMNTVWXYZ"
q = "BCDGJOPQRSU"

word = input()
x, y = 0, 0
for w in word:
    if w in p:
        x += 1
    else:
        y += 1

if x == 0 or y == 0:
    print("YES")
else:
    print("NO")