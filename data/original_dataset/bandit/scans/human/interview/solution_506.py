a, b = list(map(int, input().split()))

ans = 0

while a and b:
    if a > b:
        ans += a // b
        a = a % b
    else:
        ans += b // a
        b = b % a

print(ans)