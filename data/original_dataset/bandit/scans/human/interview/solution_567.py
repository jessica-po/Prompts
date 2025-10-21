n = int(input())
a = list(map(int, input().split()))
e = 1000000
ans = max(min(x - 1, e - x) for x in a)
print(ans)