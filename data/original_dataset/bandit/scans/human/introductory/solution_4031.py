n = int(input())
arr = [input() for _ in range(n)]

arr.sort(key = lambda x : len(x))

for u, v in zip(arr[:-1], arr[1:]):
    if u not in v:
        print('NO')
        return

print('YES')
print('\n'.join(x for x in arr))