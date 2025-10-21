input = __import__('sys').stdin.readline
MIS = lambda: map(int,input().split())

n, k = MIS()
prob = list(MIS())
while prob and prob[0] <= k: prob.pop(0)
while prob and prob[-1] <= k: prob.pop()
print(n - len(prob))