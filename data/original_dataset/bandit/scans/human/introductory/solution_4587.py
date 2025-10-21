n = int(input())
a_list = sorted([int(x) for x in input().split()])
b_list = sorted([int(x) for x in input().split()])
c_list = sorted([int(x) for x in input().split()])

import bisect
sum = 0
for b in b_list:
    b_num = bisect.bisect_left(a_list,b)
    c_num = bisect.bisect_right(c_list,b)
    sum += b_num*(len(c_list)-c_num)
print(sum)