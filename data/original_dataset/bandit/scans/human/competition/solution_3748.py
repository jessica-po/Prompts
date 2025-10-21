H, W = list(map(int, input().split()))
Ss = [input() for _ in range(H)]

# 行の入れ替えパターンを生成する（中央付近から埋めていく）
def dfs(iR):
    # 全て埋まったら、判定に移る
    if iR < 0:
        return check()

    # 未使用の行を検索する
    iF = flgs.index(False)
    Rs[iR] = iF - offset
    flgs[iF] = True

    # ペアの相手を決めて、次のペア生成に移る
    ans = False
    for iF2, flg in enumerate(flgs):
        if not flg:
            Rs[H - 1 - iR] = iF2 - offset
            flgs[iF2] = True
            ans = ans or dfs(iR - 1)
            flgs[iF2] = False

    flgs[iF] = False

    return ans


# 与えられた行の入れ替えパターンに対して、列の入れ替えのみで点対称にできるかを判定する
def check():

    Ts = [Ss[R] for R in Rs]
    Ts = list(map(list, list(zip(*Ts))))

    # (W+1)/2列目を使用可能かどうか
    if W % 2: flgCenter = True
    else: flgCenter = False

    # 各列に対して、処理を行う
    Used = [False] * W
    for j, T in enumerate(Ts):
        if Used[j]: continue
        for j2, T2 in enumerate(Ts[j + 1:], j + 1):
            # 上下反転したような未使用の列が存在するならば、次の列へ
            if not Used[j2] and T[::-1] == T2:
                Used[j2] = True
                break
        else:
            # 自身が上下対称、かつ、(W+1)/2列目を使用可能ならば、次の列へ
            if T[::-1] == T and flgCenter == True:
                flgCenter = False
            else:
                # この入れ替えパターンでは不可能と判定
                return False

    return True


if H % 2:
    # Hが奇数ならば、先頭にダミーを付加
    flgs = [False] * (H + 1)
    offset = 1
else:
    flgs = [False] * H
    offset = 0

Rs = [-1] * H
if dfs((H - 1) // 2):
    print('YES')
else:
    print('NO')