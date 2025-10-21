def main():
    n = int(input())
    arr = list(map(int, input().split()))
    dct = {}
    k = -1
    m = 0
    for i in range(n):
        try: dct[arr[i]] += 1
        except: dct[arr[i]] = 1
        if dct[arr[i]] > m:
            m = dct[arr[i]]
            k = arr[i]
    
    print(n - m)
    
    for i in range(n):
        if arr[i] == k:
            for j in range(i - 1, -1, -1):
                if arr[j] > k: print(2, j + 1, j + 2)
                else: print(1, j + 1, j + 2)
            break
    
    while i != n:
        if arr[i] > k: print(2, i + 1, i)
        if arr[i] < k: print(1, i + 1, i)
        i += 1
    return 0

main()