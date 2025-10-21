import fractions
count = 0
a = int(input())
#n

listx = list(map(int, input().split(' ')))
listy = list(map(int, input().split(' ')))
listx.remove(listx[0])
listy.remove(listy[0])
listx = set(listx)
listy = set(listy)
listz = listx.union(listy)
listz=list(listz)
listw = [i+1 for i in range(a)]
if listz == listw:
    print("I become the guy.")

else:
    print("Oh, my keyboard!")