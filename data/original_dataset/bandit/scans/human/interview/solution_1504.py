t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    l1, r1 = [int(x) for x in input().split()]
    l2, r2 = [int(x) for x in input().split()]
    if l1 > l2:
        l1, r1, l2, r2 = l2, r2, l1, r1

    if l2 < r1:
        # they already intersect.
        start = (min(r1, r2) - max(l1, l2))*n
        if start >= k:
            print(0)
            continue
        cheap = n*(max(r1, r2) - min(l1, l2)) - start
        if start + cheap >= k:
            print(k - start)
            continue
        else:
            print(cheap + (k - start - cheap)*2)
            continue

    # they do not intersect yet.
    best = 10**100
    cost_sf = 0
    intersection_sf = 0
    for j in range(n):
        # compute price using j-th interval as the last.
        cost_sf += l2 - r1
        cheap = r2 - l1
        if intersection_sf + cheap >= k:
            best = min(best, cost_sf + max((k - intersection_sf), 0))

        intersection_sf += cheap
        cost_sf += cheap
        
        best = min(best, cost_sf + max((k - intersection_sf)*2, 0))
    print(best)