N = int(input())
A = [int(a) for a in input().split()]

for i in range(1, N):
    if A[i] + A[i-1] == 5:
        print("Infinite")
        break
else:
    ans = 0
    for i in range(1, N):
        if A[i] == 2:
            if i == 1 or A[i-2] == 2:
                ans += 3
            else:
                ans += 2
        elif A[i] == 3:
            ans += 4
        else:
            if A[i-1] == 2:
                ans += 3
            else:
                ans += 4
    print("Finite")
    print(ans)