def main():
    n, m, h = map(int, input().split())
    row = list(map(int, input().split()))
    col = list(map(int, input().split()))
    mat = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if mat[i][j]:
                mat[i][j] = min(col[i], row[j])
    for arr in mat: print(*arr)
    return 0
main()