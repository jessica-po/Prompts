import itertools
n = int(input())
Tako = list(map(int, input().split()))
ans = 0
for x,y in itertools.combinations(Tako,2):
    ans += x*y

print(ans)