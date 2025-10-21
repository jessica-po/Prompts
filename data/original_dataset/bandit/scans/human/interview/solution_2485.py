import numpy as np
h, w, m = map(int, input().split())
xy = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
row = np.zeros(h, np.int)
col = np.zeros(w, np.int)
for y, x in xy:
	row[y] += 1
	col[x] += 1

max_cnt_y = max(row)
max_cnt_x = max(col)
max_pair = np.sum(row == max_cnt_y) * np.sum(col == max_cnt_x)
for y, x in xy:
	if row[y] == max_cnt_y and col[x] == max_cnt_x:
		max_pair -= 1

print(max_cnt_y + max_cnt_x - (max_pair == 0))