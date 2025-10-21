n = int(input())
w = list(map(int,input().split()))
# s1とs2の差の絶対値をリスト化
difference_list = []
# １からｎまでリストに入れて、i番目までとi番目からの合計の差をscoreに代入 
for i in range(n):
    score = abs(sum(w[:i])-sum(w[i:]))
    # scoreの値をdifference_listに追加
    difference_list.append(score)
# difference_listの最小値を出力
print(min(difference_list))