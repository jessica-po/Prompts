def median(a):
    if len(a) == 0:
        return 0
    if len(a) % 2 == 1:
        return a[len(a) // 2]
    else:
        return (a[len(a) // 2] + a[(len(a) // 2) - 1]) // 2


def profit(a, old_val):
    a.sort()
    med = median(a)
    sum_old = 0
    sum_new = 0
    for i in a:
        sum_old += abs(i - old_val)
        sum_new += abs(i - med)
    return sum_old - sum_new

n, m = [int(c) for c in input().split()]
pages = [int(c) for c in input().split()]

count = {pages[0]: []}
current_page_switches = 0

for i in range(1, len(pages)):
    cur_i = pages[i]
    prev_i = pages[i - 1]
    if not(cur_i in count):
        count[cur_i] = []

    if cur_i != prev_i:
        count[cur_i].append(prev_i)
        count[prev_i].append(cur_i)
        current_page_switches += abs(cur_i - prev_i)

max_profit = 0

for i in count:
    if len(count[i]) > 0:
        tmp = profit(count[i], i)
        if tmp > max_profit:
            max_profit = tmp


print(current_page_switches - max_profit)