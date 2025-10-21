import itertools
import bisect

N = int(input())
Nums = [str(n) for n in range(1, N+1)]

p = int(''.join([n for n in input().split()]))
q = int(''.join([n for n in input().split()]))

per = itertools.permutations(Nums)

numlist = sorted([int(''.join(list(s))) for s in per])

a = bisect.bisect_left(numlist, p)
b = bisect.bisect_left(numlist, q)

print(abs(a-b))