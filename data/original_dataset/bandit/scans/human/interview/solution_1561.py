n, m, k = list(map(int, input().split()))
a = [[0] * m for x in range(n)]
s = []
count = 0
for i in range(n):
    s.append(input())
for i in range(n):
    y = 0
    for j in range(m):
        if s[i][j] == ".":
            if(a[i][j] + 1 >= k and k > 1):
                count += 1
            y +=1
            if y >= k:
                count += 1
            if i + 1 < n:
                a[i + 1][j] = a[i][j] + 1
        else:
            y = 0
            
print(count)