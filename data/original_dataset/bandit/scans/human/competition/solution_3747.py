from collections import Counter

def main():
    s = input()

    c = Counter(s)
    w = Counter("Bulbasaur")

    ans = 1e9
    for char in w:
        ans = min(ans, c[char] // w[char])

    print(ans)


main()