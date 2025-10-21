def main():
    n = int(input())
    a = list(int(x) for x in input().split())
    s = sum(a)
    t = 0
    for i in range(n):
        t += a[i]
        if 2 * t >= s:
            print(i + 1)
            return

main()