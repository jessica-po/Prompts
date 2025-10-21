import sys

q = int(sys.stdin.readline().strip())
for Q in range(0, q):
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    p = sys.stdin.readline().strip()
    i = 0
    j = 0
    alpha = [0] * 26
    while i != len(s) and j != len(t):
        if s[i] == t[j]:
            i = i + 1
            j = j + 1
        else:
            k = ord(t[j]) - ord('a')
            j = j + 1
            alpha[k] = alpha[k] + 1
    if i != len(s):
        print("NO")
    else:
        while j < len(t):
            k = ord(t[j]) - ord('a')
            j = j + 1
            alpha[k] = alpha[k] + 1
        j = 0
        while j < len(p):
            k = ord(p[j]) - ord('a')
            j = j + 1
            alpha[k] = alpha[k] - 1
        if max(alpha) > 0:
            print("NO")
        else:
            print("YES")