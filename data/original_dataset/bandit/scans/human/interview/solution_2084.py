import sys

n_k = [int(x) for x in sys.stdin.readline().split()]
k = n_k[1]
a = [int(x) for x in sys.stdin.readline().split()]

# sum of k smallest numbers
a = sorted(a)
k_smallest = sum(a[:k])

print(k_smallest)