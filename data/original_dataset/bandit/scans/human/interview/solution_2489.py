n = int(input())
a = list(map(int, input().split()))
MAX = 10 ** 6 + 5
cnt = [0] * MAX
ok = [True] * MAX
for x in a:
    cnt[x] += 1
ans = 0
for i in range(1, MAX):
    if cnt[i] > 0:
        for j in range(i * 2, MAX, i):
            ok[j] = False       
        if ok[i] and cnt[i] == 1:
            ans += 1
print(ans)