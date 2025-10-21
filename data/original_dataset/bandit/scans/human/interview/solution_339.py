import sys

def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

n = read_int()
k = read_int()
a = read_int()
b = read_int()

cost = 0

if k == 1:
    cost = (n - 1) * a
else:
    while n != 1:
        if n % k == 0:
            if b < (n - n // k) * a:
                cost += b
            else:
                cost += (n - n // k) * a
            n = n // k
        else:
            cost += (n % k) * a
            n -= n % k
            if n == 0:
                n += 1
                cost -= a

print(cost)