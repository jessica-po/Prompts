def testcase():

    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    arr.sort()
    brr.sort(reverse=True)
    for i in range(n):
        if arr[i] + brr[i] > x:
            print('No')
            return
    print('Yes')
    return


import sys, os
if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10 ** 5)
t = int(input())
for _ in range(t - 1):
    testcase()
    input()
testcase()