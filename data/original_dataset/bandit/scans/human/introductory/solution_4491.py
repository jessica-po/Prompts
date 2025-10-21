def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n = int(input())
    a_1 = Input()
    a_2 = Input()
    ans = 0
    for i in range(n):
        ans = max(ans, sum(a_1[:i+1])+sum(a_2[i:n]))
    print(ans)

main()