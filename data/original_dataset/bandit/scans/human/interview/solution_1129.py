n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
if(n%2):
    print(arr[n//2])
else:
    print(arr[n//2-1])