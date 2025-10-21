# for _ in range(1):
for _ in range(int(input())):
    # a, b = map(int, input().split())
    n = int(input())
    arr = list(map(int, input().split()))
    # s = input()
    if [arr[0]] * n == arr:
        print(n)
    else:
        print(1)