n = int(input())
line = input().split()
ans = 0
for i in range(n):
    ans += int(line[i])*i
print(4*ans)