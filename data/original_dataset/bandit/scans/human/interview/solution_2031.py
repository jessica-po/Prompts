a = int(input())
Ans = []
A = list(map(int, input().split()))
for i in range(a):
    A[i] = [A[i], -i]
A.sort()
for i in range(a):
    A[i][1] = -A[i][1]
for i in range(int(input())):
    n, m = map(int, input().split())
    B = list(A[a - n:])
    B.sort(key=lambda n: n[1])
    Ans.append(B[m - 1][0])
for an in Ans:
    print(an)