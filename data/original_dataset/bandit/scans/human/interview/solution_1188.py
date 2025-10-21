n = int(input())

a = sorted(list(map(int, input().split())))



maxe = max(a)

cnt = []

cur, k, i = 1, 0, 0



while i < n:

    cnt.append(0)

    while i < n and a[i] < cur:

        cnt[2 * k] += 1

        i += 1

    cnt.append(0)

    while i < n and a[i] == cur:

        cnt[2 * k + 1] += 1

        i += 1

    k += 1

    cur *= 2

cnt.append(0)

cnt.append(0)

maxe = len(cnt) - 1



maxk = cnt[1]

was = False

for l in range(maxk):

    cur = 1

    while cnt[cur] > 0:

        cnt[cur] -= 1

        cur += 2

    cnt[cur] -= 1

    cursum = 0

    ok = True

    for t in range(maxe, 0, -1):

        cursum += cnt[t]

        if cursum > 0:

            ok = False

            break

    if ok:

        print(l + 1, end=" ")

        was = True



if not was:

    print(-1)



# Made By Mostafa_Khaled