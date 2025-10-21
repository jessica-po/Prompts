t = int(input())
while t:
    arr = list(map(int, input().split()))
    c = 0
    for i in arr:
        if i % 2 == 1:
            c += 1
    if c <= 1:
        print("Yes")
    else:
        if arr[0] and arr[1] and arr[2]:
            arr[3] += 3
            arr[0] -= 1
            arr[1] -= 1
            arr[2] -= 1
            c = 0
            for i in arr:
                if i % 2 == 1:
                    c += 1
            if c <= 1:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    t -= 1