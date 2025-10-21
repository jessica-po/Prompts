from collections import Counter
c=Counter(list(map(int,input().split())))
if len(c)==2:print('Yes')
else:print('No')