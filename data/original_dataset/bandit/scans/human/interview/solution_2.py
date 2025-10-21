def main():
    s = input()
    n = len(s)
    t = int(str(int(s[0]) + 1) + '0' * (n - 1))

    print(t - int(s))

main()