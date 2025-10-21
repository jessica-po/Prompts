N = int(input())
S =  input()
ans = S.count("R") * S.count("G") * S.count("B")
for i in range(N-2):
    r = S[i]
    for j in range(i+1,N-1):
        g = S[j]
        if r == g:
            continue
        k = 2*j - i
        if k >= N:
            continue
        b = S[k]
        if r != b and g != b:
            ans -= 1
print(ans)