import sys
from heapq import heappush, heappop

n = int(input())
a = list(map(int, input().split()))

count = {}

for x in a:
	if x in count:
		count[x] = count[x] + 1
	else:
		count[x] = 1

count = sorted(list(count.items()))
#print(count)

cost= list(map(int, input().split()))
max_cost = max(cost)

a = list(zip(a, cost))
a = sorted(a)
priority = list([max_cost - x for x in [x[1] for x in a]])
a = list(zip(priority, a))

i = 0
queue = []
queue_cost = 0
result = 0

#print(a)

for j in range(len(count)):
	x, c = count[j]
	#print('x = ', x)
	while i < len(a) and a[i][1][0] == x:
		queue_cost += a[i][1][1]
		heappush(queue, a[i])
		i += 1

	#print('queue = ', queue)
	y = x
	while len(queue) > 0 and (j == len(count) - 1 or count[j + 1][0] != y):
		popped = heappop(queue)
		#print(popped, queue)
		queue_cost -= popped[1][1]
		#print(queue_cost)
		result += queue_cost
		y += 1

# while len(queue) > 0:
# 	popped = heappop(queue)
# 	queue_cost -= popped[1][1]
# 	result += queue_cost

print(result)