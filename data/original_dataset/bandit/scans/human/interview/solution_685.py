from bisect import bisect_left

n, h = map(int, input().split())
x1, x2 = map(int, input().split())
if n == 1:
	print(h + x2 - x1)
else:
	gap_sum = [0]
	airflow_sum = [x2 - x1]
	for _ in range(n - 1):
		oldx1, oldx2 = x1, x2
		x1, x2 = map(int, input().split())
		gap_sum.append(gap_sum[-1] + x1 - oldx2)
		airflow_sum.append(airflow_sum[-1] + x2 - oldx2)

	#print(gap_sum)
	#print(airflow_sum)

	ans = h
	for i in range(n):
		cnt = bisect_left(gap_sum, h + gap_sum[i])
		if i == 0:
			res = airflow_sum[cnt-1] + h - gap_sum[cnt-1]
		else:
			res = airflow_sum[cnt-1] - (airflow_sum[i-1] + gap_sum[i] - gap_sum[i - 1]) + h - (gap_sum[cnt-1] - gap_sum[i])

		if res > ans:
			ans = res
	print(ans)