from string import ascii_lowercase

t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]

    s = input()
    count = {x : 0 for x in ascii_lowercase}
    errors = [int(x) for x in input().split()]

    errors = sorted(errors)

    e_idx = 0
    for j, c in enumerate(s):
        while e_idx < m and errors[e_idx] <= j:
            e_idx += 1
        count[c] += (m - e_idx) + 1

    print(*[count[c] for c in ascii_lowercase])