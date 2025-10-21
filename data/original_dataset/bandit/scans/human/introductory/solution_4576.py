a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0

for i in range(a + 1):
    for j in range(b + 1):
        maisuuOf50 = (x - i * 500 - j * 100) / 50
        if 0 <= maisuuOf50 <= c:
            ans += 1

print(ans)