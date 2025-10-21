from collections import Counter, defaultdict
from string import ascii_lowercase as al

n, k = list(map(int, input().split()))
s = list(input())

C = defaultdict(int, Counter(s))
C_ = defaultdict(int)

k_ = k
for char in al:
    temp = min(C[char], k_)

    C_[char] += temp
    k_ -= temp

for i, el in enumerate(s):
    if C_[el] > 0:
        s[i] = ''
        C_[el] -= 1

print(''.join(s))