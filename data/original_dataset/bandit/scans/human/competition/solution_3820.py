#!/usr/bin/env python3
def solve(n, m, s, t):
    if '*' in s:
        l, r = s.split('*')
        return len(l) + len(r) <= len(t) and t.startswith(l) and t.endswith(r)
    else:
        return s == t

n, m = list(map(int, input().split()))
s = input()
t = input()
print(['NO', 'YES'][solve(n, m, s, t)])