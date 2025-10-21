for _ in range(int(input())):
    n = int(input())
    wt = list(map(int, input().split()))
    count = {}
    for x in wt:
        if x not in count:
            count[x] = 0
        count[x] += 1
    k = 0

    for s in range(101):
        temp = 0
        temp2 = 0
        for x in count:
            if (s - x) in count:
                if (s - x) == x:
                    temp2 += count[x] // 2
                else:
                    temp += min(count[x], count[s -x])
        
        k = max(k, temp//2 + temp2)
    print(k)