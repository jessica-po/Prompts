from collections import deque


def main():
    s = deque(input())

    res = []
    for i in range(len(s) - 1, -1, -1):
        if i % 2 == 1:
            res.append(s.pop())
        else:
            res.append(s.popleft())

    print(''.join(res[::-1]))


main()