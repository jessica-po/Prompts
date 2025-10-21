def answer(s: str) -> str:
    return ''.join(s[0].upper() for s in s.split())


def main():
    s = input()
    print(answer(s))


def __starting_point():
    main()
__starting_point()