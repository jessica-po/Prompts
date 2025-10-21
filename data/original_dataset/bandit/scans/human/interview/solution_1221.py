from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
first = list(map(int, stdin.readline().split()))
second = list(map(int, stdin.readline().split()))
ans = float('inf')

for i in range(n):
    cnt = float('-inf')
    
    for j in range(m):    
        for z in range(n):
            if z == i:
                continue
            
            cnt = max(cnt, first[z] * second[j])
    
    ans = min(ans, cnt)

stdout.write(str(ans))