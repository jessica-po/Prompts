# python3
from sys import stdin
from collections import namedtuple


def readline(): return tuple(map(int, input().split()))


n, a, b = readline()
hand = [tuple(map(int, line.split())) for line in stdin.readlines()]

if not b:
    print(sum(creature[1] for creature in hand))
else:
    hand.sort(key=lambda self: self[0] - self[1])

    best = 0
    if n > b:
        l = hand[n - b]
        lost = max(0, l[0] - l[1])
        for creature in hand[:n-b]:
            best = max(best, (creature[0] << a) - creature[1] - lost)

    for creature in hand[max(0,n-b):]:
        best = max(best, (creature[0] << a) - max(creature))

    print((sum(creature[1] for creature in hand)
          + sum(max(0, creature[0] - creature[1]) for creature in hand[max(0,n-b):])
          + best))