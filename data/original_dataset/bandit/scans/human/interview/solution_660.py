n, b, p = map(int, input().split())
answer1 = 0
answer2 = n
while n > 1:
    k = 1
    while k < n:
        k *= 2
    answer1 += k * b + (k // 2)
    n = k // 2 + n - k
print(answer1, answer2 * p)