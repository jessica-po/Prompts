def main():
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    dct = {}
    for x in arr:
        dct[x] = 0
    
    i = 0
    while i != n and dct[arr[i]] == 0:
        dct[arr[i]] = 1
        i += 1
    
    if i == n:
        print(0)
        return 0
    
    j = n - 1
    while dct[arr[j]] == 0:
        dct[arr[j]] = 1
        j -= 1
    
    ans = j - i + 1
    
    for k in range(i - 1, -1, -1):
        dct[arr[k]] -= 1
        while dct[arr[j]] == 0:
            dct[arr[j]] = 1
            j -= 1
        ans = min(ans, j - (k - 1))
    
    print(ans)
    
    return 0

main()