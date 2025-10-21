def excl_max_list(a):
    first_max = max(a)
    imax = a.index(first_max)
    second_max = max(a[:imax] + a[imax + 1:])
    return [second_max if elem == first_max else first_max for elem in a]

def excl_min_list(a):
    first_min = min(a)
    imin = a.index(first_min)
    second_min = min(a[:imin] + a[imin + 1:])
    return [second_min if elem == first_min else first_min for elem in a]

n = int(input())
rectangles = [tuple(map(int, input().split())) for i in range(n)]
lefts = [l for l, d, r, u in rectangles]
rights = [r for l, d, r, u in rectangles]
downs = [d for l, d, r, u in rectangles]
ups = [u for l, d, r, u in rectangles]

max_lefts = excl_max_list(lefts)
max_downs = excl_max_list(downs)
min_rights = excl_min_list(rights)
min_ups = excl_min_list(ups)

for i in range(n):
    if max_lefts[i] <= min_rights[i] and max_downs[i] <= min_ups[i]:
        print(max_lefts[i], max_downs[i])
        break