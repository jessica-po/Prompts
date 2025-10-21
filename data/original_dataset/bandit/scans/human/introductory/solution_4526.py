for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    keke = dict()
    for elem in ar:
        if elem in keke:
            keke[elem] += 1
        else:
            keke[elem] = 1
    ans = 0
    for i in range(n):
        num = ar[i]
        for j in range(i + 1, n):
            num += ar[j]
            if num in keke:
                ans += keke[num]
                keke[num] = 0
    print(ans)