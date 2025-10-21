def prog():
    n = int(input())
    inp = list(map(int,input().split()))
    temp = []
    while(n!=1):
        temp += [n]
        n = inp[n-2]
    temp += [1]
    temp.reverse()
    for i in temp:
        print(i,end=' ')
prog()