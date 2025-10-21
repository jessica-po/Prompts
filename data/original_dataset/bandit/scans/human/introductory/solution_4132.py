N = int(input())
A = list(map(int,input().split()))
A_list = [float('inf')] * N

ans = min(A)
while max(A_list) > 0:
    mi = ans
    for i,a in enumerate(A):
        amari = a % mi
        A_list[i] = amari
        if amari != 0:
            ans = min(ans,amari)

print(ans)