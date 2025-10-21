def main():
    s = input()
    n = len(s)
    poss = False
    for i in range(n - 2):
        t = s[i:i + 3]
        if 'A' in t and 'B' in t and 'C' in t:
            poss = True
            break
    print('Yes' if poss else 'No')


main()