n,s = map(int,input().split())
A = list(map(int,input().split()))
if A[s-1] != 0:
    per = 1
    A[s-1] = 0
else:
    per = 0
A.sort()
maxs = max(A)
ans = [0] * (maxs + 1)
answer = maxs + 1
o = -1
for j in range(n):
    if A[j] == 0:
        o += 1
    
    if ans[A[j]] == 0:
        ans[A[j]] = 1
        answer -= 1
an = per + max(o, answer)

for j in range(n-2,-1,-1):
    
    for t in range(A[j+1]-1, A[j] -1,-1):
        if ans[t] == 0:
            answer -= 1
    
    an = min(an, per + max(answer,o+n - j - 1))
print(an)