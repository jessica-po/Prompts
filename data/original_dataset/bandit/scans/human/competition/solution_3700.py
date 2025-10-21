#!/usr/bin/env python3
n, k = list(map(int, input().split()))
ans = max(0, min(n, k - 1) - k // 2)
print(ans)