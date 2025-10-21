from collections import defaultdict

N,K = list(map(int, input().split()))
A = list(map(int, input().split()))
BMAX = 40
"""
・K以下の非負整数の範囲で〜：桁DP感ある
・XORをとる：桁ごとに確認できる
・Xを選んで、f = X xor A1 + X xor A2 + ... + X xor AN
　 -> それぞれのAと毎回 xor 取るのではなく、桁ごとに xor を取ることができる　←　超重要のはず
　 -> A1 ~ AN の各桁（2進数の時の）に1が立っているのが何個あるか数えておく


遷移
dp[i][1] -> dp[i+1][1] : i-1桁目まででK未満が確定していれば、i桁目に1,0どちらを選んでもK未満
dp[i][0] -> dp[i+1][1]  : i-1桁目まででKと一致している場合、Kのi桁目が1なら、Xで0を選べば遷移できる
dp[i][0] -> dp[i+1][0]  : i桁目まで一致させる場合
"""

d = [0] * BMAX
for a in A:
  for i in range(BMAX):
    if a & (1 << i):
      d[i] += 1

# dp[i+1][0] : Xをi桁目まで決めた時に、Kのi桁目までと厳密に一致する　ときの最大値
# dp[i+1][1] : Xをi桁目まで決めた時に、Kのi桁目までと厳密に一致しないときの最大値

dp = [[-1 for _ in range(2)] for _ in range(BMAX+1)]


dp[0][0] = 0

for i in range(BMAX):
  now = BMAX-1-i
  # Xの左からnow桁目に1,0を設定した時にfが増加する量
  p0 = (2**now) * d[now]
  p1 = (2**now) * (N - d[now])
  
  # Kの左からnow番目に1が立ってるかどうか
  if K & (1 << now):
    is_one = True
  else:
    is_one = False

  # dp[i][1] -> dp[i+1][1] はXのi桁目に1,0を使えるから、より多い方を採用
  if dp[i][1] != -1:
    dp[i+1][1] = dp[i][1] + max(p1, p0)

  # dp[i][0] -> dp[i+1][1] はKのi桁目が1なら可能
  if dp[i][0] != -1 and is_one:
    dp[i+1][1] = max(dp[i+1][1], dp[i][0] + p0)

  # dp[i][0] -> dp[i+1][0] 
  if dp[i][0] != -1:
    dp[i+1][0] = dp[i][0] + (p1 if is_one else p0)    

print((max(dp[-1])))