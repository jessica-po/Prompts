N,K,C = map(int,input().split())
S = input()
L = []
R = []
i = 0
while i < N:
    if S[i] == "o":
        L.append(i)
        i += C
    i += 1
j = N-1
while j >= 0:
    if S[j] == "o":
        R.append(j)
        j -= C
    j -= 1   
for i in range(K):
    if L[i] == R[K-1-i]:
        print(L[i]+1)