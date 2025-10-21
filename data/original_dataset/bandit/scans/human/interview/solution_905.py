import itertools
import math
import random

import time
def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time()-t))
        return res

    return tmp

def genArray(length, lower, upper):
    return [random.randint(lower, upper) for i in range(length)]


n, s = list(map(int, input().split(' ')))
array = [list(map(int, input().split(' '))) for i in range(n)]

res = -100;
for i in range(n):
    if array[i][0]+array[i][1]/100 <= s:
        sdacha = 100 - array[i][1]
        if array[i][1]== 0:
            sdacha = 0
        if sdacha>res:
            res = sdacha

if res == -100:
    print(-1)
else:
    print(res)