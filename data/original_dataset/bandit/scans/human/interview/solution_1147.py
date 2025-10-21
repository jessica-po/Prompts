import math
import bisect


n, x, k = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
ans = 0

for num in a:
    l = math.ceil(num/x)*x + (k-1)*x
    r = l + x - 1
    l = num if l < num else l
    # print(l, r, bisect.bisect_left(a, l), bisect.bisect_right(a, r), bisect.bisect_right(a, r) - bisect.bisect_left(a, l))
    ans += bisect.bisect_right(a, r) - bisect.bisect_left(a, l)

print(ans)


'''
7 3 2
1 3 5 9 11 16 25
'''

'''
4 2 0
5 3 1 7
'''