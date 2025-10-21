mii = 3*10**4

factors = [set() for _ in range(mii + 1)]
factors[1] = set([1])

for k in range(2, mii + 1):
    for p in range(2, mii + 1):
        if k % p == 0:
            factors[k] = set(ole*p for ole in factors[k//p]) | factors[k//p]
            break
        elif p * p > k:
            factors[k] = set([1, k])
            break

# print(factors[:20])

t = int(input())
for _ in range(t):

    a, b, c = [int(x) for x in input().split()]


    best_score = 10**15
    best_trip = a, b, c

    for k in range(1, mii + 1):
        this_b = k
        if c % this_b < this_b - (c % this_b):
            this_c = this_b * (c // this_b)
        else:
            this_c = this_b * (c // this_b + 1)

        this_c = max(this_c, this_b)

        this_a = -1
        loss_a = 10**15
        for cur_a in factors[this_b]:
            if abs(a - cur_a) < loss_a:
                this_a = cur_a
                loss_a = abs(a - cur_a)

        cur_score = abs(a - this_a) + abs(b - this_b) + abs(c - this_c)
        if cur_score < best_score:
            best_score = cur_score
            best_trip = this_a, this_b, this_c

    print(best_score)
    print(*best_trip)