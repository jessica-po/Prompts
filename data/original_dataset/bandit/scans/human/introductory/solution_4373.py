def main():
    n = int(input())
    arr = sorted(map(int, input().split()))
    j = 1
    for x in arr:
        if x >= j:
            j += 1
    print(j - 1)
    return 0

main()