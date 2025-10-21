a, b, k = map(int,input().split())
for i in range(a,min(b,a+k-1)+1):
    print(i)
for i in range(max(b-k+1,a+k),b+1):
    print(i)