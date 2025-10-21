n = int(input())
a = sorted(list(set(map(int, input().split()))))

for i in range(2, len(a)):
    if a[i] - a[i - 2] <= 2:
        print('YES')
        break
else:
    print('NO')