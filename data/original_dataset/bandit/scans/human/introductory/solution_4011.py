def main():
    n = int(input())
    a = list(map(int, input()))
    f = [0] + list(map(int, input().split()))
    i = 0
    while f[a[i]] <= a[i]:
        i += 1
        if i == n:
            break
    for j in range(i, n):
        if f[a[j]] < a[j]:
            break
        else:
            a[j] = f[a[j]]
    print("".join(str(x) for x in a))
    return 0

main()