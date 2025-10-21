# problem http://codeforces.com/contest/1100/problem/E
import copy
import sys


def find_loop(g, w, k, n):
    visited = [False] * n
    visited_int = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        stack = [g[i][:]]
        path = [i]
        visited[i] = True
        visited_int[i] = True
        while stack:
            if not stack[-1]:
                stack.pop()
                visited_int[path[-1]] = False
                path.pop()
                continue
            nxt = stack[-1][-1]
            stack[-1].pop()
            if w[(path[-1], nxt)] <= k:
                continue
            if visited_int[nxt]:
                return True
            if visited[nxt]:
                continue
            visited[nxt] = True
            visited_int[nxt] = True
            stack.append(g[nxt][:])
            path.append(nxt)
    return False


def top_sort(g, w, k, n):
    visited = [False] * n
    order = [-1] * n
    cnt = 0
    for i in range(n):
        if visited[i]:
            continue
        stack = [g[i][:]]
        path = [i]
        visited[i] = True
        while stack:
            if not stack[-1]:
                order[path[-1]] = cnt
                path.pop()
                stack.pop()
                cnt += 1
                continue
            nxt = stack[-1][-1]
            stack[-1].pop()
            if w[(path[-1], nxt)] <= k:
                continue
            if visited[nxt]:
                continue
            visited[nxt] = True
            stack.append(g[nxt][:])
            path.append(nxt)

    to_reverse = []
    for a, b in list(w.items()):
        if b > k:
            continue
        if order[a[0]] < order[a[1]]:
            to_reverse.append(a)
    return to_reverse


def __starting_point():
    n, m = list(map(int, input().split()))
    w = {}
    g = [[] for _ in range(n)]
    w_tmp = {}
    c_m = 0
    kk = [0]
    lines = sys.stdin.readlines()
    for i, line in enumerate(lines): #range(1, m + 1):
        u, v, c = list(map(int, line.split()))
        g[u - 1].append(v - 1)
        if (u - 1, v - 1) in list(w.keys()):
            w[(u - 1, v - 1)] = max(w[(u - 1, v - 1)], c)
        else:
            w[(u - 1, v - 1)] = c
        if (u - 1, v - 1) in list(w_tmp.keys()):
            w_tmp[(u - 1, v - 1)].append(str(i + 1))
        else:
            w_tmp[(u - 1, v - 1)] = [str(i + 1)]
        kk.append(c)
        # c_m = max(c, c_m)

    # print(find_loop(copy.deepcopy(g), copy.deepcopy(w), 0, n))

    kk.sort()
    l, r = 0, len(kk)
    if not find_loop(g, w, kk[l], n):
        print(0, 0)
        return
    if find_loop(g, w, kk[-1], n):
        kkk = kk[-1]
    else:
        while l + 1 != r:
            m = int((l + r) / 2)
            # if find_loop(copy.deepcopy(g), copy.deepcopy(w), kk[m], n):
            if find_loop(g, w, kk[m], n):
                l = m
            else:
                r = m
        kkk = kk[l+1]

    to_reverse = top_sort(g, w, kkk, n)
    num = 0
    s = []
    for t in to_reverse:
        num += len(w_tmp[t])
        s.extend(w_tmp[t])

    print(kkk, num)
    print(" ".join(s))






__starting_point()