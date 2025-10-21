TC = int(input())
while TC > 0:
    n, a, b = list(map(int, input().split()))
    ans = ""
    for i in range(b):
        ans += chr(ord('a') + i)
    ans = ans * n
    print(ans[:n])

    TC -= 1