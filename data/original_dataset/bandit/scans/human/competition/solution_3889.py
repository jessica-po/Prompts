import collections

n = int(input())
s = collections.Counter(input())
print('Yes' if n == 1 or max(s.values()) > 1 else 'No')