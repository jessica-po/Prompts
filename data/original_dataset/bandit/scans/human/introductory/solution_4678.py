N = int(input())
A = list(map(int,input().split()))
T = 0
for i in range(len(A)-1):
    if  (A[i] > A[i + 1]):
        T += A[i] - A[i +1]
        A[i+1] = A[i] 
print(T)