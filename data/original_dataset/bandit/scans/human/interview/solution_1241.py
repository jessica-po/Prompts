#!/usr/bin/env python3

try:
    while True:
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        left = 0
        result = -1
        cur = 0
        for i in range(n):
            if not a[i]:
                if k:
                    k -= 1
                else:
                    if i - left > result:
                        res_left = left
                        res_right = i
                        result = i - left
                    while left < i and a[left]:
                        left += 1
                    left += 1

        if i + 1 - left > result:
            res_left = left
            res_right = i + 1
            result = i + 1 - left

        print(result)
        for i in range(res_left):
            print(a[i], end=' ')
        for i in range(result):
            print(end="1 ")
        for i in range(res_right, n):
            print(a[i], end=' ')
        print()

except EOFError:
    pass