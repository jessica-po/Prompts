N = int(input())

S = list(map(int,input().split()))[::-1]

print(min(N - S.index(0), N - S.index(1)))