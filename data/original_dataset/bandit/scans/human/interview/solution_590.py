n = int(input())
a = list(map(int, input().split()))

nums = [False for i in range(200010)]
must = [False for i in range(200010)]
counter = dict()
now_num = 0


def inc():
    nonlocal now_num
    now_num += 1
    while nums[now_num - 1]:
        now_num += 1


for el in a:
    if nums[el - 1]:
        counter[el] += 1
    else:
        counter[el] = 1
    nums[el - 1] = True

inc()

ans = []
c = 0

for el in a:
    if counter[el] > 1:
        counter[el] -= 1
        if now_num < el:
            ans.append(now_num)
            c += 1
            inc()
        else:
            if must[el - 1] == False:
                ans.append(el)
                must[el - 1] = True
            else:
                ans.append(now_num)
                c += 1
                inc()
    else:
        if must[el - 1] == False:
            ans.append(el)
        else:
            ans.append(now_num)
            c += 1
            inc()

print(c)
print(' '.join(str(el) for el in ans))