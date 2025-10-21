def main():
    v = {
        "1" : 2,
        "2" : 5,
        "3" : 5,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 3,
        "8" : 7,
        "9" : 6,
        "0" : 6
    }
    a, b = map(int, input().split())
    answer = 0

    for i in range(a, b + 1):
        s = str(i)

        for e in s:
            answer += v[e]

    print(answer)



def __starting_point():
    main()
__starting_point()