#!/usr/bin/env python3

n = int(input())
a = [int(x) for x in input().split()]

sorted_a = sorted(a)
dict_a = {}
for x in a:
    if not x in dict_a:
        dict_a[x] = 1
    else:
        dict_a[x] += 1

sorted_uniq_a = sorted(dict_a.keys())

max_fib_prefix = [a[0], a[1]]
for i in range(0, len(sorted_uniq_a)):
    for j in range(0, len(sorted_uniq_a)):
        if i != j or dict_a[sorted_uniq_a[i]] > 1:
            if sorted_uniq_a[i] + sorted_uniq_a[j] > sorted_uniq_a[-1]:
                break

            fib_prefix = [sorted_uniq_a[i], sorted_uniq_a[j]]
            dict_a[sorted_uniq_a[i]] -= 1
            dict_a[sorted_uniq_a[j]] -= 1

            while True:
                next_fib = fib_prefix[-1] + fib_prefix[-2]
                if not next_fib in dict_a or dict_a[next_fib] == 0:
                    break
                fib_prefix.append(next_fib)
                dict_a[next_fib] -= 1

            for x in fib_prefix:
                dict_a[x] += 1

            if len(fib_prefix) > len(max_fib_prefix):
                max_fib_prefix = fib_prefix

print(len(max_fib_prefix))