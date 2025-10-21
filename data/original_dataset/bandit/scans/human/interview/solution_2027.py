def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.append(0)
    ans = []
    for i in range(n):
        ans.append(arr[i] + arr[i + 1])
    print(*ans)
    
main()