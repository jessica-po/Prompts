# -1 0 1を足したもののうち最大値を数える
n = int(input())
a = list(map(int, input().split()))
# ai=0の場合もあるので-1がありえることに注意 適当にa[0]を-1の数とする
d = [0] * (10**5 + 10)
for av in a:
    for x in [-1, 0, 1]:
        # 前述の通りa[0]を-1の数とする
        d[av + x + 1] += 1
print(max(d))