n = int(input())
A = [int(x) for x in input().split()]
mn = min(A)

I = [i for i in range(len(A)) if A[i] == mn]
mindiff = min(I[i]-I[i-1] for i in range(1,len(I)))
print(mindiff)