for __ in range(int(input())):
    n = int(input())
    ar = []
    for ________ in range(n):
        ar.append(list(map(int, input().split())))
    ar.sort(key=lambda x: x[1])
    num1 = ar[0][1]
    ar.sort(key=lambda x: -x[0])
    num2 = ar[0][0]
    print(max(0, num2 - num1))