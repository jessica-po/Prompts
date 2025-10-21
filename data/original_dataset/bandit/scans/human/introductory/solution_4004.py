def main():
    n = int(input())
    a = list(sorted(set(map(int, input().split()))))
    if len(a) > 3:
        print(-1)
    elif len(a) == 1:
        print(0)
    elif len(a) == 2:
        d = a[1] - a[0]
        if d & 1:
            print(d)
        else:
            print(d >> 1)
    else:
        d = a[1] - a[0]
        D = a[2] - a[1]
        if d == D:
            print(d)
        else:
            print(-1)
    return 0

main()