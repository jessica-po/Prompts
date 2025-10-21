from collections import defaultdict

def solve(n, k):
    as_bin = bin(n)[2:]
    cnt = defaultdict(int)
    cnt.update({i : 1 for i, b in enumerate(reversed(as_bin)) if b == '1'})
    curr_len = len(cnt)
    curr_pow = len(as_bin) - 1

    if curr_len > k:
        return None

    while True:
        new_len = curr_len + cnt[curr_pow]
        if new_len > k:
            break
        cnt[curr_pow - 1] += 2 * cnt[curr_pow]
        del cnt[curr_pow]
        curr_pow -= 1
        curr_len = new_len

    i = min(cnt.keys())
    while curr_len < k:
        cnt[i] -= 1
        cnt[i - 1] += 2
        curr_len += 1
        i -= 1

    ans = []
    for i in sorted(list(cnt.keys()), reverse=True):
        ans.extend([i] * cnt[i])
    return ans

n, k = [int(v) for v in input().split()]
ans = solve(n, k)

if ans is None:
    print('No')
else:
    print('Yes')
    print(' '.join(str(c) for c in ans))