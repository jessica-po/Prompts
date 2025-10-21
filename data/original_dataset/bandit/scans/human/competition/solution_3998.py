n = int(input())
L = list(map(int, input().split()))
ans = 0
M = []
while max(L) != min(L):
    ans += 1
    k = max(L)
    if L.count(k) == 3:
        s = ''
        for i in range(len(L)):
            if L[i] == k:
                s += '1'
                L[i] -= 1
            else:
                s += '0'
        M.append(s)    
    else:      
        max_1 = 0
        max_2 = 1
        if L[max_1] < L[max_2]:
            max_1, max_2 = max_2, max_1
        for i in range(2, n):
            if L[i] > L[max_1]:
                max_2, max_1 = max_1, i
            elif L[i] > L[max_2]:
                max_2 = i
        s = ''
        for i in range(n):
            if i == max_1 or i == max_2:
                s += '1'
            else:
                s += '0'
        M.append(s)
        L[max_1] -= 1
        if L[max_1] < 0:
            L[max_1] = 0
        L[max_2] -= 1
        if L[max_2] < 0:
            L[max_2] = 0
print(max(L))
print(ans)
for i in M:
    print(i)