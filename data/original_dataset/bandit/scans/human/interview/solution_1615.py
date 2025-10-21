N,k=input().split()
N=int(N)
k=int(k)
x=0
for i in range(N):
    A,B=input().split()
    A=int(A)
    B=int(B)
    x+=(max(A,B)-min(A,B)+1)

answer=(x%k)
if(answer!=0):
    answer=k-answer

print(answer)