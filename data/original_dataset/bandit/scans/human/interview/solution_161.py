def main():
    x = int(input())
    n = x.bit_length()
    t = 0
    ans = []
    while True:
        if (x + 1) & (x) == 0:
            break
        if t & 1:
            x += 1
        else:
            for i in range(n - 1, -1, -1):
                if not (1 << i) & x:
                    ans.append(i + 1)
                    x ^= (1 << (i + 1)) - 1
                    break
        t += 1
    print(t)
    print(*ans)
    return 0

main()