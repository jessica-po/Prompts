n=int(input())

s=input().split()

A=[0,0,0]
for i in range(n):
    A[i%3]+=int(s[i])

m=max(A)

if(m==A[0]):
    print("chest")
elif(m==A[1]):
    print("biceps")
else:
    print("back")