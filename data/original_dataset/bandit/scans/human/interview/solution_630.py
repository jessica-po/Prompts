# python3

def readline(): return tuple(map(int, input().split()))


def main():
    n, k = readline()
    a = readline()

    answer = list()

    for (i, link) in enumerate(a):
        bottom = max(0, i - k)
        top = min(n, i + k + 1)

        if link == 0:
            answer.append(top - bottom)
        else:
            bottom = max(bottom, link + k)
            answer.append(max(0, top - bottom) + answer[link - 1])

    print(" ".join(map(str, answer)))


main()