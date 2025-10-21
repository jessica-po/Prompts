3

import sys

s = sys.stdin.readline().strip()
k = int(sys.stdin.readline())
s += '*' * k

def is_tandem(s):
    # print(s)
    n = len(s) // 2
    a, b = s[:n], s[n:]
    for i in range(n):
        if a[i] == '*' or b[i] == '*': continue
        if a[i] != b[i]:
            return False
    return True

l = 0
for i in range(len(s)):  # Beginning of tandem
    for n in range(2, len(s) - i + 1, 2):  # Length of tandem
        if is_tandem(s[i:i+n]):
            l = max(l, n)
print(l)