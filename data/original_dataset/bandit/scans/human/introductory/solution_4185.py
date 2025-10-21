import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
arr = [[] for i in range(m)]

for _ in range(n):
    l = list(map(int, input().split()))
    for i in range(m):
        arr[i].append(l[i])

out = 0
for i in range(m):
    l = arr[i]
    
    best = list(range(0, -n, -1))
    for j in range(n):
        v = l[j] - i - 1
        
        if v % m == 0:
            correct = v // m
            if 0 <= correct < n:
                best[j - correct] += 1
    out += (n - max(best))

print(out)