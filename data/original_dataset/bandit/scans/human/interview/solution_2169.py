def resolve():
    H, W, D = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(H)]
    Q = int(input())
    LR = [list(map(int, input().split())) for _ in range(Q)]

    num_to_pos = {}
    for i in range(H):
        for j in range(W):
            num_to_pos[A[i][j]] = (i, j)
    
    acc = [[0] for _ in range(D+1)]
    for i in range(1, D+1):
        num = i
        idx = 0
        while num + D <= H*W:
            _from = num_to_pos[num]
            _to = num_to_pos[num+D]
            acc[i].append(acc[i][idx]+abs(_from[0]-_to[0])+abs(_from[1]-_to[1]))
            num += D
            idx += 1
    
    # print(acc)
    for lr in LR:
        l, r = lr
        series = l%D if l%D != 0 else D
        # print("---")
        # print(series)
        # print(l, r)
        print((acc[series][(r-series)//D] - acc[series][(l-series)//D]))
            



if '__main__' == __name__:
    resolve()