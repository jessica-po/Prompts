n = int(input())
arr = list(map(float, input().split()))
if n == 1:
    print(int(arr[0]))
    return
arr.sort(reverse = True)
res = 0
while arr:
    res += sum(arr)
    arr = arr[:len(arr)//4]
print(int(res))