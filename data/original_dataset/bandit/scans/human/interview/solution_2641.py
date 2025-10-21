import sys
import numpy as np
from numba import njit


def input(): return sys.stdin.readline()

N,Q = list(map(int,input().split()))

C=np.array(input().split(), int)

# Query取得-rightでソート
# dtypeQuery = [("index", int), ("start", int), ("end", int)]
queries=np.empty((Q,2),int)
# #rights=[[] for _ in range(N+1)]

for q in range(Q):
	l,r=list(map(int,input().split()))
	#queries[q] = (q,l,r)
	queries[q][0] = l
	queries[q][1] = r
	#queries=np.sort(queries,order="end")

#queries=np.array(sys.stdin.buffer.read().split(),int).reshape(Q,2)

orderByR=np.argsort(queries[:,1])

# 各色の現在の一番右のindex
mostRightColorIndex = np.zeros(N+1, int)
# bit indexed tree
bitArray=np.zeros(N+1,int)

@njit
def main(N,Q,C,queries,orderByR,mostRightColorIndex,bitArray):

	def add(itemCount, items, i, value):
		while i <= itemCount:
			items[i] += value
			i += (i & (-i))

	def sumFromStart(items, end):
		summary = 0
		i = end
		while i > 0:
			summary += items[i]
			i -= (i & (-i))
		return summary

	def sum(items, start,end):
		summary = sumFromStart(items, end) - sumFromStart(items, start-1)
		return summary

	# 答え配列
	#ans=np.zeros(Q, int)
	ans=[0]*Q
	# 左からBITと現在色の更新をしながら、クエリのrightに到達したときにBITにクエリ発行する
	qindex = 0

	for n in range(N):
		# 外側のループでは、全部の色をループ

		if Q <= qindex:
			break

		if 0 < mostRightColorIndex[C[n]]:
			# ループ中の場所の色のindexが既にある場合(=過去に、同じ色が登録されていた場合)
			# 今回で、同じ色の一番右側の要素はループ中の要素になる
			# 前登録したこの色の一番右のindexを一度BITから抜く(↓で再度登録される)
			add(N,bitArray,mostRightColorIndex[C[n]], -1 )

		# この要素の色の一番右のindexを、BITに登録
		mostRightColorIndex[C[n]] = n+1
		add(N,bitArray,n+1, 1)

		# while qindex < Q and n+1 == queries[qindex][2]:
		while qindex < Q and n+1 == queries[orderByR[qindex]][1]:
			# 今のBITが次のクエリ発行するための状態(n==query.right)だったら、クエリ発行
			tmpIndex = orderByR[qindex]
			start = queries[tmpIndex][0]
			end = queries[tmpIndex][1]
			ans[tmpIndex]=sum(bitArray,start,end)
			# print(tmpIndex,start,end,ans[tmpIndex])
			qindex += 1

	return ans

for a in main(N,Q,C,queries,orderByR,mostRightColorIndex,bitArray):
	print(a)