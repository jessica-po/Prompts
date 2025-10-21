n = int(input())
print(n - 1 if sum(map(int, input().split())) % n else n)