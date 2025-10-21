for i in range(int(input())):
    
    n=int(input())
    moves=0
    while n%2==0:
        n=n//2
        moves+=1
    while n%3==0:
        n=n//3
        moves+=2
    while n%5==0:
        n=n//5
        moves+=3
    if n==1:
        print(moves)
    else :
        print(-1)