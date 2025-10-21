n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = sum(a)
d = sum(b)

if c >= d:
    print('Yes')
else:
    print('No')