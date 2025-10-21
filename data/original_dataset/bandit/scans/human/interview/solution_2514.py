from collections import Counter 

N = int(input())
A = list(map(int,input().split()))
Q = int(input())

tot = sum(A)
A = Counter(A)

for i in range(Q):
    B,C = map(int,input().split())
    tot +=(C - B) * A[B]
    A[C] += A[B]
    A[B] = 0
    print(tot)