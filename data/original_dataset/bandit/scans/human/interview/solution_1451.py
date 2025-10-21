n, k = list(map(int, input().split()))
print(sum(s.count('4')+s.count('7')<=k for s in input().split()))