def readinput():
    n=int(input())
    return n

def main(n):
    stock=[]
    for _ in range(10):
        stock.append([])

    stock[0].append('')
    for m in range(1,10):
        for i in range(len(stock[m-1])):
            stock[m].append(stock[m-1][i]+'3')
            stock[m].append(stock[m-1][i]+'5')
            stock[m].append(stock[m-1][i]+'7')
    #print(stock)
    count=0
    for m in range(3,10):
        for i in range(len(stock[m])):
            if int(stock[m][i]) <= n and '3' in stock[m][i] and '5' in stock[m][i] and '7' in stock[m][i]:
                count+=1
                #print(stock[m][i])
    return count

def __starting_point():
    n=readinput()
    ans=main(n)
    print(ans)

__starting_point()