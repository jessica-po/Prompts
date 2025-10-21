def func(arr):
    arr.sort()
    ans = 0
    for i in range(len(arr) - 1, -1, -2):
        ans += arr[i]
    return ans

def main():
    n, h = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        if func(arr[:i]) > h:
            i -= 1
            break
    print(i)
    return 0
main()