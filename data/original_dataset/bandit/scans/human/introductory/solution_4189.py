# python3


def main():
    n = int(input())

    hard, soft = 0, 0
    while n:
        n -= 1
        if input().split()[1] == "hard":
            hard += 1
        else:
            soft += 1

    if hard < soft:
        hard, soft = soft, hard

    assert soft <= hard
    side = 1
    while side ** 2 / 2 < soft or side ** 2 / 2 + (side & 1) < hard:
        side += 1

    print(side)


main()