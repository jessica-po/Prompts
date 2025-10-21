n=int(input())
A = [0] * (2*n)
per1 = 0
per2 = n
for i in range(1, n):
    if i % 2==1:
        A[per1] = i
        A[per1+n-i] = i
        per1+=1
    else:
        A[per2] = i
        A[per2+n-i] = i
        per2+=1

A[-1] = n
if n % 2 == 1:
    A[n//2] = n
else:
    A[-(n//2+1)] = n
print(' '.join(map(str, A)))