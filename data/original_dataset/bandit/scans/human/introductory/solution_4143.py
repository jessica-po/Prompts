#70 C - Five Transportations
N = int(input())
lis = [int(input()) for _ in range(5)]
mini = min(lis)
group = (N+mini-1)//mini

ans = 5 + group - 1
print(ans)