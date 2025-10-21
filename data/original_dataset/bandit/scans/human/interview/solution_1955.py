n,m = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sums = sum(B)+len(B)
last = [-1] * m
cou = 0
ans = 0
per = 0
for j in range(n):
    if A[j] == 0:
        cou +=1
    else:
        if last[A[j]-1] == -1:
            if j >= B[A[j]-1]:
                
                ans += 1
                last[A[j]-1] = 0
                
        if ans == m:
            if (j+1) >= sums:
                per=1
                print(j+1)
                break
           
        
    
    
if per == 0:
    print(-1)