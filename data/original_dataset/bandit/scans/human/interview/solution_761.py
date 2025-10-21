import sys
import string


def ria():
    return [int(i) for i in input().split()]


n = ria()[0]
ar = ria()

if n == 1:
    print(ar[0])
    return

onlyNegs = True
onlyPos = True

if max(ar) >= 0:
    onlyNegs = False
if min(ar) <= 0:
    onlyPos = False

if onlyNegs:
    print(abs(sum(ar)) + max(ar) * 2)
    return

if onlyPos:
    print(abs(sum(ar)) - min(ar) * 2)
    return

print(sum([abs(i) for i in ar]))