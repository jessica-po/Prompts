for _ in range(int(input())):
    n = int(input())
    data = input()
    count = 0
    while "AP" in data:
        data = data.replace("AP", "AA")
        count += 1
    print(count)