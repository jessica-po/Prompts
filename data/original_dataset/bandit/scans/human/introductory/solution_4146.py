n = int(input())
v = list(map(int, input().split()))
odd = [0] * (10 ** 5 + 5)
even = [0] * (10 ** 5 + 5)
for i in range(n):
    if i % 2 == 0:
        even[v[i]] += 1
    else:
        odd[v[i]] += 1
sum_odd = sum(odd)
sum_even = sum(even)
ans = sum_odd + sum_even
max_odd = max(odd)
max_even = max(even)
if odd.index(max_odd) != even.index(max_even):
    print(sum_odd + sum_even - max_even - max_odd)
else:
    odd.sort()
    even.sort()
    if odd[-1] - odd[-2] > even[-1] - even[-2]:
        ans -= odd[-1] + even[-2]
    else:
        ans -= odd[-2] + even[-1]
    print(ans)