import collections 
n = int(input())
li = list(input().split())
c = collections.Counter(li)
if len(c) == 3:
    print('Three')
else:
    print('Four')