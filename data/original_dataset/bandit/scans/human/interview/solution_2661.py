def main():
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline

    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    U = list(map(int, input().split()))
    V = list(map(int, input().split()))

    range_N = list(range(N))
    ans = [[0]*N for _ in range_N]
    # 論理積
    for i in range_N:
        if S[i] == 0:
            for j in range_N:
                ans[i][j] = ans[i][j] | U[i]
        if T[i] == 0:   
            for j in range_N:
                ans[j][i] = ans[j][i] | V[i]
    for i in range_N:
        for j in range_N:
            if (U[i] & V[j]):
                ans[i][j] = ans[i][j] | (U[i] & V[j])

    # 論理和
    for x in range_N:
        if S[x] == 0:
            continue
        x_sum = ans[x][0]
        for y in range_N:
            x_sum = x_sum | ans[x][y]
        if x_sum == U[x]:
            continue
        up = U[x] - x_sum
        for y in range_N:
            if T[y]:
                continue
            y_mul = ans[0][y]
            for i in range_N:
                if i == x:
                    continue
                y_mul = y_mul & ans[i][y]
            up_y = (~y_mul) & up
            ans[x][y] += up_y
            up -= up_y
            if up == 0:
                break

    for y in range_N:
        if T[y] == 0:
            continue
        y_sum = ans[0][y]
        for x in range_N:
            y_sum = y_sum | ans[x][y]
        if y_sum == V[y]: 
            continue
        up = V[y] - y_sum
        for x in range_N:
            if S[x]:
                continue
            x_mul = ans[x][0]
            for j in range_N:
                if y == j:
                    continue
                x_mul = x_mul & ans[x][j]
            up_x = (~x_mul) & up
            ans[x][y] += up_x
            up -= up_x
            if up == 0:
                break

    # チェック
    for i in range_N:
        check_xs = ans[i][0]
        check_ys = ans[0][i]
        check_xm = ans[i][0]
        check_ym = ans[0][i]
        for j in range_N:
            check_xs = check_xs | ans[i][j]
            check_ys = check_ys | ans[j][i]
            check_xm = check_xm & ans[i][j]
            check_ym = check_ym & ans[j][i]
        if (S[i] and U[i] != check_xs) \
        or (T[i] and V[i] != check_ys) \
        or (S[i] == 0 and U[i] != check_xm) \
        or (T[i] == 0 and V[i] != check_ym) :
            print((-1))
            return       

    for i in range_N:
        print((*ans[i]))

main()