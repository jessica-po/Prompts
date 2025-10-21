Z = 100000

n = int(input())
xx = list(map(int, input().split()))


def cal():
    ans = []
    a = 1
    b = 1
    s = 0
    ls = 1
    for x in xx:
        while b <= Z:
            if s < x:
                s += b * 2 + 1
                b += 1
            elif s > x:
                s -= a * 2 + 1
                ls += a * 2 + 1
                a += 1
            else:
                ans.append(ls)
                ans.append(x)
                ls = b * 2 + 1
                b += 1
                a = b
                s = 0
                break
        else:
            return
    return ans


ans = cal()
if ans:
    print('Yes')
    print(' '.join(map(str, ans)))
else:
    print('No')