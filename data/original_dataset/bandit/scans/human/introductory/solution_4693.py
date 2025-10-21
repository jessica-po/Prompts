# A - Restricted
# https://atcoder.jp/contests/abc063/tasks/abc063_a

A, B = list(map(int, input().split()))

result = A + B
if result >= 10:
    print('error')
else:
    print(result)