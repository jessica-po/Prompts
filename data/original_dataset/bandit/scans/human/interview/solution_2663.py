import heapq


def contig(p, A):
 ans = []
 n = len(A)
 for i in range(n):
  for j in range(i, n):
   if i == j:
    ans.append(p[i])
   else:
    ans.append(p[j] - p[i])
 return ans


def solver(N, K, A):
 a = []
 prefix = [A[0]]
 for x in A[1:]:
  prefix.append(prefix[-1] + x)

 return heapq.nlargest(K, contig(prefix, A))


def __starting_point():
 N, K = list(map(int, input().split()))
 A = list(map(int, input().split()))

 print(' '.join([str(i) for i in solver(N, K, A)]))

__starting_point()