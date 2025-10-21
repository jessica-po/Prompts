import bisect

n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

# n : number of integers
# m : mod

half_n = n // 2

a1, a2 = a[:half_n], a[half_n:]

n1, n2 = len(a1), len(a2)

r1, r2 = [], []

def dfs1(i, sum):
    if i == n1:
        r1.append(sum)
    else:
        dfs1(i+1, sum)
        dfs1(i+1, (sum+a1[i])%m)

def dfs2(i, sum):
    if i == n2:
        r2.append(sum)
    else:
        dfs2(i+1, sum)
        dfs2(i+1, (sum+a2[i])%m)

dfs1(0,0)
dfs2(0,0)

r1, r2 = [sorted(set(x)) for x in [r1, r2]]

ans = 0

for i, x in enumerate(r1):
    p = bisect.bisect_left(r2, m-x)
    tmp_ans = r2[p-1] + x
    if tmp_ans > ans:
        ans = tmp_ans

print(ans)