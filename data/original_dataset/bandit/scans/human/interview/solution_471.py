from math import *
n, a = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
if n == 1:
    print(0)
    
else:
    if a > A[-1]:
        print(abs(a - A[1]))
    elif a < A[0]:
        print(abs(a - A[-2]))
    else:
        per1 = abs(A[0] - A[-2])
        per2 = abs(A[1] - A[-1])
        ans1 = abs(A[0] - a) + per1
        ans2 = per1 + abs(A[-2] - a)
        ans3 = per2 + abs(a - A[-1])
        ans4 = per2 + abs(a - A[1])
        print(min(ans1, ans2, ans3, ans4))