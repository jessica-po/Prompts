n = int(input())
l = list(map(int,input().split()))
cnt = 0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            x = [l[i],l[j],l[k]]
            ma = sorted(x)[2]
            _ma = sorted(x)[0] + sorted(x)[1]
            if l[i] != l[j] and l[i] != l[k] and l[j] != l[k] and ma < _ma:
                cnt += 1
print(cnt)