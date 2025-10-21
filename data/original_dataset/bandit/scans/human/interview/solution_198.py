x = int(input())
if x%2==1:
    print(0)
    quit()
if x%2 ==0:
    x//=2
    if x%2==0:
        print(x//2-1)
    else:
        print(x//2)