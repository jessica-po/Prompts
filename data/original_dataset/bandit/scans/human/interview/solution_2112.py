def get_val(x, k, y, left_val, right_val, arr):
    x, y = y, x
    if not arr:
        return 0
    if len(arr) < k:
        if max(arr) > max(left_val, right_val):
            return -1
        return len(arr) * x
    if y < x * k:
        n = len(arr)
        res = 0
        while n >= k:
            n -= k
            res += y
        res += n * x
        return res
    else:
        if max(arr) < max(left_val, right_val):
            return len(arr) * x
        else:
            return ((len(arr) - k) * x) + y


def solve(x, k, y, a, b):
    def check(a, b):
        j = 0
        i = 0
        while i < len(a) and j < len(b):
            if a[i] != b[j]:
                i += 1
            else:
                i += 1
                j += 1
        return j == len(b)

    if not check(a, b):
        return -1

    j = 0
    left_val = -1
    arr = []
    res = 0
    for num in a:
        if j == len(b) or num != b[j]:
            arr.append(num)
        else:
            val = get_val(x, k, y, left_val, num, arr)
            if val == -1:
                return -1
            res += val
            arr = []
            left_val = num
            j += 1
    if arr:
        val = get_val(x, k, y, left_val, -1, arr)
        if val == -1:
            return -1
        res += val
    return res


n, m = list(map(int, input().split()))
x, k, y = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(x, k, y, a, b))