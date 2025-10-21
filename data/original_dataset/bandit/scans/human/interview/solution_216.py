n=int(input())
arr= list(map(int,input().strip().split(' ')))
s = 0
for i in range(n):
   s+=abs(arr[i])
print(s)