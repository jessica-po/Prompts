import sys

n, k = list(map(int, input().split(' ')))

s = input()

def max_streak(s):
    result = 0

    for i in range(len(s)):
        j = i
        while j < len(s) and s[j] == 'N':
            j += 1

        result = max(result, j - i)

    return result

for i in range(n - k + 1):
    cur = list(s)
    for j in range(i, i + k):
        if cur[j] == '?':
            cur[j] = 'N'

    for j in range(i):
        if cur[j] == '?':
            cur[j] = 'Y'

    for j in range(i + k, n):
        if cur[j] == '?':
            cur[j] = 'Y'

    if max_streak(cur) == k:
        print('YES')
        return

print('NO')