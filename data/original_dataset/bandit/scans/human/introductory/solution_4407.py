from collections import Counter

n, q = map(int, input().split())
a = map(int, input().split())
b = [int(input()) for _ in range(q)]

counts = 32 * [0]

for value, count in Counter(a).items():
    counts[value.bit_length() - 1] = count

for bj in b:
    ans = 0
    
    for i in reversed(range(32)):
        count = min(bj >> i, counts[i])
        ans += count
        bj -= count << i
    
    if bj != 0:
        print(-1)
    else:
        print(ans)