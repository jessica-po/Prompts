def main():
    n, m = list(map(int, input().split()))

    p_words = set()
    e_words = set()

    for _ in range(n):
        p_words.add(input())
    for _ in range(m):
        e_words.add(input())

    common = p_words & e_words

    p_words -= common
    e_words -= common

    we_win = False
    p_turn = True

    a, b, c = len(p_words), len(e_words), len(common)

    while True:
        if c > 0:
            c -= 1
        else:
            if p_turn:
                if a == 0:
                    we_win = False
                    break
                else:
                    a -= 1
            else:
                if b == 0:
                    we_win = True
                    break
                else:
                    b -= 1

        p_turn = not p_turn

    print("YES" if we_win else "NO")

main()