N = int(input())
H = [int(i) for i in input().split()]
count = 0
ans = 0
for i in range(N-1):
    if(H[i] >= H[i+1]):
        count += 1
    else:
        ans = max(ans,count)
        count = 0
print(max(ans,count))