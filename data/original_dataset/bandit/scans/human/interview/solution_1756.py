def sum_first(di):
    return di * (di + 1) // 2


n, x = list(map(int, input().split()))
n *= 2
d = tuple(map(int, input().split())) * 2
ans = 0
i = 0
j = 0
cur_ans = 0
total_days = 0
while j <= n:
    if total_days < x:
        if j == n:
            break
        cur_ans += sum_first(d[j])
        total_days += d[j]
        j += 1
    else:
        ans = max(ans, cur_ans - sum_first(total_days - x))
        cur_ans -= sum_first(d[i])
        total_days -= d[i]
        i += 1
print(ans)