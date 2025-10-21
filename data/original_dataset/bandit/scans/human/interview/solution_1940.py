n, k = [int(i) for i in input().split()]

w = [int(i) for i in input().split()]

tot = 0
for wi in w:
    tot += (wi+k-1)//k

ans = (tot+1)//2
print(ans)