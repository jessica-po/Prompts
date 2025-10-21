Q = input().split(" ")
F = input().split(" ")
xQ = int(Q[0])
yQ = int(Q[1])
xF = int(F[0])
yF = int(F[1])

if xQ == xF:
    print((abs(yQ-yF)+1)*2+4)
elif yQ == yF:
    print((abs(xQ-xF)+1)*2+4)
else:
    print((abs(xQ-xF)+1)*2+(abs(yQ-yF)+1)*2)