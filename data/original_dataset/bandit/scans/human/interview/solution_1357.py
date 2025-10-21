n, m = list(map(int, input().split()))
v = list(map(int, input().split()))

for i in range(1, len(v)):
    if v[i] < v[i-1]: v[i] += ((v[i-1] - v[i]) // n) * n
    while v[i] < v[i-1]: v[i] += n

print(v[-1]-1)