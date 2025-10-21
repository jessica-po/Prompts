s = input()

l = []
t = 0

for i in range(len(s)):
    if len(l) > 0:
        if s[i] == l[-1]:
            l.pop()
            t += 1
        else:
            l.append(s[i])
    else:
        l.append(s[i])

if t % 2 == 0:
    print("No")
else:
    print("Yes")