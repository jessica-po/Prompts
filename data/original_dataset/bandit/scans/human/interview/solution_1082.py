def getmask(x):
    ans = 0
    for i in range(2, x + 1):
        while x % (i * i) == 0:
            x //= i * i
        if x % i == 0:
            ans ^= 1 << i
            x //= i
    return ans

def main():
    maxn = 71
    n = int(input())
    a = [int(i) for i in input().split()]
    cnt = [0] * maxn
    for i in a:
        cnt[i] += 1
    masks = {}
    for i in range(1, maxn):
        if cnt[i]:
            masks[getmask(i)] = masks.get(getmask(i), 0) + cnt[i]
    while len(masks) > 1 or 0 not in masks:
        if not masks:
            print(0)
            return
        fixed = max(masks.keys())
        for i in list(masks.keys()):
            if i ^ fixed < i:
                masks[i ^ fixed] = masks.get(i ^ fixed, 0) + masks[i]
                masks[i] = 0
        masks[0] = masks.get(0, 0) + masks[fixed] - 1
        masks[fixed] = 0
        masks = {i: j for i, j in list(masks.items()) if j > 0}
    print(pow(2, masks[0], 10**9+7) - 1)
    
    
    
main()