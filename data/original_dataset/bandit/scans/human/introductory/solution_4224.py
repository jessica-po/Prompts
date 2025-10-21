n = int(input())
a = list(map(int,input().split()))

cnt = 0
for i in range(n):
    while True:
        if a[i]%2==0:
            a[i]=a[i]//2
            cnt +=1
        else:
            break
print(cnt)