n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
a = [0] * 5
b = [0] * 5
for j in range(n):
    a[A[j]-1] += 1
    b[B[j]-1] +=1
per = 0
for j in range(5):
    if (a[j] + b[j]) % 2 == 1:
        per = 1
        break
if per == 1:
    print(-1)
else:
    ans = 0
    for j in range(5):
        if a[j] > b[j]:
            ans += (a[j] - b[j])//2
    print(ans)