a, A = list(map(int,input().split()))
b, B = list(map(int,input().split()))
c = input()
c = int(c[:2]) * 60 + int(c[-2:])
d = 0
for i in range(5 * 60, 24 * 60, b):
    if i < c + A and i + B > c:
        d += 1
print(d)