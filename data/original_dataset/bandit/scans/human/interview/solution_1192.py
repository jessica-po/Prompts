from sys import stdin, stdout
from math import *
from itertools import *
from copy import *

s = 0
invs = 0

def calc_invertions(a):
    s = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            s += 1 if a[i] > a[j] else 0
    return s

def do_flips(arr, num):
    nonlocal s, invs
    if num == 0:
        invs += 1
        s += calc_invertions(arr)
    else:
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                for k in range((j - i + 1) // 2):
                    arr[i + k], arr[j - k] = arr[j - k], arr[i + k]
                do_flips(arr, num - 1)
                for k in range((j - i + 1) // 2):
                    arr[i + k], arr[j - k] = arr[j - k], arr[i + k]
    
def solve(test):
    ints = list(map(int, test.strip().split()))
    n, m = ints[:2]
    arr = ints[2:]
    do_flips(arr, m)
    return s / invs

stdout.write(str(solve(stdin.read())))