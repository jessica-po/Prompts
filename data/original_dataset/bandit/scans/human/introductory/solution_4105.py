n, k = list(map(int, input().split()))
if n > k*(k-1):
    print("NO")
else:
    print("YES")
    cnt = 0
    for delta in range(k):
        for c in range(1, k+1):
            if cnt < n:
                cnt +=1
                print(c, 1+(c+delta)%k)
            else:
                break