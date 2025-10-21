n = int(input())
p = [int(i) for i in input().split()]
for i in range(n):
    tmp = [0] * n
    j = i
    while tmp[j] != 1:
        tmp[j] = 1
        j = p[j] - 1
    print(j + 1, end = " ")