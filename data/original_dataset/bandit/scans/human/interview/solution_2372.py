# import numpy as np
from collections import deque

def solve(): #H, W, CH, CW, DH, DW, S):
	H,W=list(map(int,input().split()))
	CH,CW=list(map(int,input().split()))
	DH,DW=list(map(int,input().split()))
	S=[input() for _ in range(H)]

	# 後の条件分岐を簡略化するためワープしても迷路外に出ないように壁で囲む
	S = ['##{}##'.format(row) for row in S]
	S.insert(0, '##{}##'.format('#' * W))
	S.insert(0, '##{}##'.format('#' * W))
	S.append('##{}##'.format('#' * W))
	S.append('##{}##'.format('#' * W))


	MAX_COST = 10 ** 9
	Cost=[ [ MAX_COST for _ in range(W+4)] for _ in range(H+4)]
	# Cost = np.full((H,W),MAX_COST)

	# print(S)

	ans = -1

	cost0 = deque()

	cost0.append((CH+1,CW+1,0))
	Cost[CH+1][CW+1] = 0;

	# used = set()
	walk=[(1,0),(0,1),(-1,0),(0,-1)]
	warp = [ (i,j) for i in range(-2,3) for j in range(-2,3) if (i, j) not in [(0, 0)] + walk ]
	# print(warp)

	cost1 = deque()

	while cost0:
		h,w,c=cost0.popleft()
		cost1.append((h,w,c))

		for i,j in walk:
			dh = h+i
			dw = w+j
			if S[dh][dw] == '.' and c < Cost[dh][dw]:
				Cost[dh][dw] = c
				# print("updl ", i,j,dh,dw,c)
				cost0.appendleft((dh,dw,Cost[dh][dw]))

		if len(cost0) == 0:

			while cost1:
				h,w,c=cost1.popleft()
				# print(h,w,c)
				for i,j in warp:
					dh = h+i
					dw = w+j
					# print(i,j)
					if S[dh][dw] == '.' and c + 1 < Cost[dh][dw]:
						Cost[dh][dw] = c + 1
						cost0.append((dh,dw,Cost[dh][dw]))


	if Cost[DH+1][DW+1] == MAX_COST:
		print((-1))
	else:
		print((Cost[DH+1][DW+1]))


def __starting_point():

	# S=[input() for _ in range(H)]

	solve() #H, W, CH, CW, DH, DW, S)

__starting_point()