n = int(input())
l = input()
l = l.split()
c = 0
for i in range(len(l)):
    l[i] = int(l[i])
    if l[i]%2 == 0:
        c += 1
    else:
        c -= 1

if c > 0:
    print("READY FOR BATTLE")
else:
    print("NOT READY")