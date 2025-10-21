b =[1,1,2,7,4]
a =list(map(int,input().split()))
ans = 100
for i in range(5):
    ans = min(a[i]//b[i],ans)
print(ans)