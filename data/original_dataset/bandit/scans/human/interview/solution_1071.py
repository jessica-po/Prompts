a = list(map(int, input().split()))
b = list(map(int, input().split()))
n = int(input())
n1 = (sum(a) - 1) // 5 + 1
n2 = (sum(b) - 1) // 10 + 1
if n1 + n2 <= n:
    print('YES')
else:
    print('NO')