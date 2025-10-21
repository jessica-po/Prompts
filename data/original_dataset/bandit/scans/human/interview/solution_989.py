n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = {}
for elem in a:
    if elem in cnt:
        cnt[elem] += 1
    else:
        cnt[elem] = 1
cnt = sorted(list(cnt.items()))
for i in range(len(cnt)):
    cnt[i] = list(cnt[i])
left = 0
right = len(cnt) - 1
while k > 0:
    if k < cnt[left][1] and k < cnt[right][1]:
        break
    if left == right:
        break
    if cnt[left][1] <= cnt[right][1]:
        if k >= cnt[left][1] * (cnt[left + 1][0] - cnt[left][0]):
            k -= cnt[left][1] * (cnt[left + 1][0] - cnt[left][0])
            cnt[left + 1][1] += cnt[left][1]
            left += 1
        else:
            cnt[left][0] += k // cnt[left][1]
            k = 0
    else:
        if k >= cnt[right][1] * (cnt[right][0] - cnt[right - 1][0]):
            k -= cnt[right][1] * (cnt[right][0] - cnt[right - 1][0])
            cnt[right - 1][1] += cnt[right][1]
            right -= 1
        else:
            cnt[right][0] -= k // cnt[right][1]
            k = 0
print(cnt[right][0] - cnt[left][0])