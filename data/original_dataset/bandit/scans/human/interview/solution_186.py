n, m = list(map(int, input().split()))

start = 0
end = 10**10
while (end - start > 1):
    mid = (end + start) // 2
    two = mid // 2 - mid // 6
    three = mid // 3 - mid // 6
    six = mid // 6

    nn = n
    mm = m

    nn -= two
    mm -= three
    nn = max(nn, 0)
    mm = max(mm, 0)
    if (six >= nn + mm):
        end = mid
    else:
        start = mid
print(end)