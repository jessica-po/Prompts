from operator import attrgetter, itemgetter
n = int(input());
arr = [[int(x) for x in input().split(' ')] for y in range(n)];
arr = sorted(arr, key=itemgetter(1,0,2), reverse=True);
dp = [0 for x in range(n)];
s = [];
for i in range(n):
	while (s != [] and arr[s[-1]][0] >= arr[i][1]):
		s.pop();
	if (s != []):
		dp[i] = dp[s[-1]];
	dp[i] += arr[i][2];
	s.append(i);
print(max(dp));