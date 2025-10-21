T = int(input())
for t in range(T):
    N, R = list(map(int, input().split()))
    print(1 + (R - sum(map(int, input().split()))) % N)