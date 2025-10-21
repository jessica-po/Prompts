import sys
 
input = sys.stdin.readline
N = int(input())
P = list(map(int, input().split()))
 
target = 1
ans = []
i = 0
while i < N: 
    if P[i] == target:
        for j in range(i, target-1, -1):
            P[j], P[j-1] = P[j-1], P[j]
            ans.append(j)
    
        target = i+1
        # print("i", i, "target", target)
    i += 1
 
# print(P)
if len(ans) != N-1:
    print(-1)
    return
for i in range(N):
    if P[i] != i+1:
        print(-1)
        return
 
print(*ans, sep="\n")