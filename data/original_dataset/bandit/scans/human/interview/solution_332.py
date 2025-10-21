from collections import Counter


def input_matrix():
    res = tuple((Counter() for _ in range(n + m)))
    for i in range(n):
        for j, a in enumerate(map(int, input().split())):
            res[i + j][a] += 1
    return res


n, m = list(map(int, input().split()))
if input_matrix() == input_matrix():
    print("YES")
else:
    print("NO")