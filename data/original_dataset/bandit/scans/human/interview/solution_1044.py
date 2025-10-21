n = int(input())
now = 2
for i in input().split():
    a = int(i)
    if a % 2 == 0:
        now = 3 - now
    print(now)