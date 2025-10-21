for _ in range(int(input())):
    n = int(input())
    digits = list(map(int,list(input())))
    if n % 2 == 1:
        containsOdd = False
        for i in range(0,n,2):
            if digits[i] % 2 == 1:
                containsOdd = True
        if containsOdd:
            print(1)
        else:
            print(2)
    else:
        containsEven = False
        for i in range(1,n,2):
            if digits[i] % 2 == 0:
                containsEven = True
        if containsEven:
            print(2)
        else:
            print(1)