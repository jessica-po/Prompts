def main():
    (b1, q, l, m) = list(map(int, input().split()))
    a = set(map(int, input().split()))
    if abs(b1) > l:
        print(0)
    else:
        if b1 == 0:
            if 0 in a:
                print(0)
            else:
                print("inf")
        elif q == 0:
            if 0 not in a:
                print("inf")
            elif b1 in a:
                print(0)
            else:
                print(1)
        elif q == 1:
            if b1 in a:
                print(0)
            else:
                print("inf")
        elif q == -1:
            if (b1 in a) and ((-b1) in a):
                print(0)
            else:
                print("inf")
        else:
            ans = 0
            b = b1
            for i in range(100):
                if b in a:
                    b *= q
                    if abs(b) > l:
                        break
                    continue
                ans += 1
                b *= q
                if abs(b) > l:
                    break
            print(ans)

def __starting_point():
    main()

__starting_point()