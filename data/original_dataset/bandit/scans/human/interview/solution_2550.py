for _ in range(int(input())):
    n, m = map(int, input().split())
    l1 = list(map(int,input().split()))
    print(min(sum(l1),m))