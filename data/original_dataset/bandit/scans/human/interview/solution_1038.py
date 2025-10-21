def XorWorld():
    a, b = list(map(int, input().split()))
    if a%2 == 0 and b%2 == 0:
        if ((b-a)//2)%2 == 0:
            print((0^b))
        else:
            print((1^b))
    elif a%2 == 0:
        if ((b-a+1)//2)%2 == 0:
            print((0))
        else:
            print((1))
    elif b%2 == 0:
        if ((b-a-1)//2)%2 == 0:
            print((0^a^b))
        else:
            print((1^a^b))
    else:
        if ((b-a)//2)%2 == 0:
            print((0^a))
        else:
            print((1^a))

def __starting_point():
    XorWorld()
    

__starting_point()