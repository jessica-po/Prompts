#!/usr/bin/env python3

c = [list(map(int, input().split())) for i in range(3)]


a1 = 0
b1, b2, b3 = c[0][0], c[0][1], c[0][2]
a2 = c[1][0]-b1
a3 = c[2][0]-b1

check = []
check.append(c[1][1] == a2+b2)
check.append(c[2][1] == a3+b2)
check.append(c[1][2] == a2+b3)
check.append(c[2][2] == a3+b3)

if sum(check) == 4:
    print("Yes")
else:
    print("No")