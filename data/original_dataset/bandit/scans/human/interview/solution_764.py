from collections import deque
import math

num = int(input())
x = tuple(map(int, list(input())))

#if x == "0"*num: print(num); return

integer = 0

dic = dict()

for i in range(1,num+1):
    a = math.gcd(i,num)
    if a in dic:
        integer += dic[a]
    else:
        lijst = [0]*a
        
        for j in range(num):
            b = j%a
            lijst[b] += x[j]

        for k in range(a):
            if lijst[k]%2 != 0:
                dic[a] = 0
                break
        else:
            integer += 1
            dic[a] = 1
print(integer)