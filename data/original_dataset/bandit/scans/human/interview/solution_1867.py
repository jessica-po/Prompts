import collections

n = int(input())
As = list(map(int, input().split()))

def solve(n, As):
    counter = collections.Counter(As)
    candidates = []
    prev_freq = 0
    for num, freq in counter.most_common():
        if prev_freq and prev_freq!= freq:
            break
        candidates.append(num)
        prev_freq = freq
    lr = {cand:[] for cand in candidates}
    for i, a in enumerate(As, 1):
        if a in lr:
            lr[a].append(i)
    minspan = float('inf')
    for pos in list(lr.values()):
        if pos[-1] - pos[0] < minspan:
            minspan = pos[-1] - pos[0]
            LR = (pos[0], pos[-1])
    return LR

print(*solve(n, As))