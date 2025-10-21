for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = False
    for j in range(len(arr)):
        for c in range(j + 2, len(arr)):
            if arr[c] == arr[j]:
                flag = True
                break
    print("YES" if flag else "NO")