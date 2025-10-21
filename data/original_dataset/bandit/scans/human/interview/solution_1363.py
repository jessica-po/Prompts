import bisect
from functools import lru_cache

g, d, f = tuple(map(int, input().split()))

goals = list(map(int, input().split()))
defs = list(map(int, input().split()))
forwards = list(map(int, input().split()))

goals.sort()
defs.sort()
forwards.sort()

forwards.append(100000000)
defs.append(100000000)
goals.append(100000000)

numers = []
roles = []
gi, di, fi = 0, 0, 0

for i in range(d + g + f):
    numers.append(min(goals[gi], defs[di], forwards[fi]))

    if numers[-1] == goals[gi]:
        roles.append(1)
        gi += 1

    if numers[-1] == forwards[fi]:
        roles.append(3)
        fi += 1

    if numers[-1] == defs[di]:
        roles.append(2)
        di += 1

#print(numers)
#print(roles)


@lru_cache()
def my_comb(n, k):
    if k == 0:
        return 1
    if n < k:
        return 0
    if n == k:
        return 1
    if k == 3:
        return (n * (n - 1) * (n - 2)) // 6
    if k == 2:
        return (n * (n - 1)) // 2
    if k == 1:
        return n
    assert False


def solve(numers, roles):
    ans = 0
    for i in range(len(numers)):
        # check all combinations with guy i

        possible_max_num = bisect.bisect_right(numers, numers[i] * 2)

        if possible_max_num - i < 5:
            continue

        avaliable_f = roles[i + 1: possible_max_num].count(3)
        avaliable_d = roles[i + 1: possible_max_num].count(2)
        avaliable_g = roles[i + 1: possible_max_num].count(1)

        needed_f, needed_d, needed_g = 3, 2, 1

        if roles[i] == 1:
            needed_g -= 1
        elif roles[i] == 2:
            needed_d -= 1
        else:
            needed_f -= 1

        possible_combinations_with_ith = my_comb(avaliable_d, needed_d) * my_comb(avaliable_f, needed_f) * my_comb(
            avaliable_g, needed_g)
        ans += possible_combinations_with_ith

    return ans


print(solve(numers, roles))