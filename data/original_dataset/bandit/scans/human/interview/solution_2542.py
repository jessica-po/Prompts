def det(s, i, j):
    ans = 0
    curr = i
    for a in s:
        if a == curr:
            ans += 1
            if curr == i: curr = j
            else: curr = i

    if i == j: return ans
    return ans // 2 * 2

for t in range(int(input())):
    s = list(map(int, list(input())))
    ans = 0
    
    for i in range(10):
        for j in range(10):
            ans = max(ans, det(s, i, j))

    print(len(s)-ans)