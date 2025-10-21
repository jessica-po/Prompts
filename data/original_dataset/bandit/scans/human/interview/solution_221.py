n, k = map(int, input().split())
if n <= k + k + 1:
    print(1)
    print((n + 1) // 2)
else:
    answer = -1
    answer_n = 10**100
    for i in range(min(k + 1, n)):
        t = n - (k + i + 1)
        if t % (k + k + 1) >= k + 1:
            if 2 + t // (k + k + 1) < answer_n:
                answer = i + 1
                answer_n = 2 + t // (k + k + 1)
        if t % (k + k + 1) == 0:
            if 1 + t // (k + k + 1) < answer_n:
                answer = i + 1
                answer_n = 1 + t // (k + k + 1)            
    print(answer_n)
    while answer <= n:
        print(answer, end = ' ')
        answer += k + k + 1