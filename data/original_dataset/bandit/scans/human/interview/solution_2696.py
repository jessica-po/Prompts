# cook your dish here
n=int(input())
arr=[int(x) for x in input().split()]
ans=n-1
while(ans>0 and arr[ans]==arr[ans-1]):ans-=1
print(ans+1)