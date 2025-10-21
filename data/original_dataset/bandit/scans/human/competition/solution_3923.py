# python3
# utf-8

n, a, b = (int(x) for x in input().split())

l = -1
for k in range(n // a + 1):
    if (n - k * a) % b == 0:
        l = (n - k * a) // b
        break
if l == -1:
    print(-1)
    quit()

perm = []
curr_last_op = 1
for i in range(k):
    curr_cycle = [curr_last_op + j for j in range(a)]
    curr_last_op = curr_last_op + a
    perm += curr_cycle[1:] + curr_cycle[:1]

for i in range(l):
    curr_cycle = [curr_last_op + j for j in range(b)]
    curr_last_op = curr_last_op + b
    perm += curr_cycle[1:] + curr_cycle[:1]

print(*perm)