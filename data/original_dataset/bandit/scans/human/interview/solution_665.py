t = int(input())
for i in range(t):
    n, s = [int(x) for x in input().split()]
    a= [int(x) for x in input().split()]
    need = -1
    if (sum(a)) <= s:
        print(0)
    else:
        for i in range(n):
            if a[i] > need:
                need= a[i]
                index = i
            if s - a[i] < 0:
                print(index + 1)
                break
            s -= a[i]